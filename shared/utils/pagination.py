from typing import Any, Dict, List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, subqueryload
from sqlalchemy import desc

from shared.utils.success_response import success_response


def paginated_response(
    db: Session,
    model,
    skip: int,
    limit: int,
    join: Optional[Any] = None,
    filters: Optional[Dict[str, Any]] = None,
):
    """
    Custom response for pagination.\n
    This takes in four atguments:
        * db- this is the database session
        * model- this is the database table model eg Product, Organisation```
        * limit- this is the number of items to fetch per page, this would be a query parameter
        * skip- this is the number of items to skip before fetching the next page of data. This would also
        be a query parameter
        * join- this is an optional argument to join a table to the query
        * filters- this is an optional dictionary of filters to apply to the query

    Example use:
        **Without filter**
        ``` python
        return paginated_response(
            db=db,
            model=Product,
            limit=limit,
            skip=skip
        )
        ```

        **With filter**
        ``` python
        return paginated_response(
            db=db,
            model=Product,
            limit=limit,
            skip=skip,
            filters={'org_id': org_id}
        )
        ```

        **With join**
        ``` python
        return paginated_response(
            db=db,
            model=Product,
            limit=limit,
            skip=skip,
            join=user_organisation_association,
            filters={'org_id': org_id}
        )
        ```
    """

    query = db.query(model)

    if join is not None:
        query = query.join(join)

    if filters and join is None:
        # Apply filters
        for attr, value in filters.items():
            if value is not None:
                column = getattr(model, attr)
                
                if isinstance(column.type, bool):
                    # Handle boolean fields
                    query = query.filter(column == value)
                elif isinstance(column.type, str):
                    # Handle string fields
                    query = query.filter(column.like(f"%{value}%"))
                else:
                    # Handle other types (e.g., Integer, DateTime)
                    query = query.filter(column == value)

    elif filters and join is not None:
        # Apply filters
        for attr, value in filters.items():
            if value is not None:
                query = query.filter(
                    getattr(getattr(join, "columns"), attr).like(f"%{value}%")
                )

    total = query.count()
    results = (
        query
        .order_by(desc(model.created_at))
        .offset(skip)
        .limit(limit)
        .all()
    )
    items = jsonable_encoder(results)

    try:
        total_pages = int(total / limit) + (total % limit > 0)
    except:
        total_pages = int(total / limit)
       
    return success_response(
        status_code=200,
        message="Successfully fetched items",
        data={
            "pages": total_pages,
            "total": total,
            "skip": skip,
            "limit": limit,
            "items": items,
        },
    )


def get_pagination_details(num_of_items, offset, limit):
    total_pages = int(num_of_items / limit) + (num_of_items % limit > 0)
    return {
        "limit": limit,
        "offset": offset,
        "pages": total_pages,
        "total_items": num_of_items,
    }


def format_timestamp(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02}:{seconds:02}"

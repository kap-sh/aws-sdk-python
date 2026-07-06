"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchSortResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.order_by_field_type
    import aws_sdk_workdocs.types.sort_order


class SearchSortResult(TypedDict, closed=True):
    field: NotRequired["aws_sdk_workdocs.types.order_by_field_type.OrderByFieldType"]
    """<p>Sort search results based on this field name.</p>"""
    order: NotRequired["aws_sdk_workdocs.types.sort_order.SortOrder"]
    """<p>Sort direction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortResult) -> dict:
    out: dict = {}
    if "field" in value:
        import aws_sdk_workdocs.types.order_by_field_type

        out["Field"] = aws_sdk_workdocs.types.order_by_field_type.serialize_json(
            value["field"]
        )
    if "order" in value:
        import aws_sdk_workdocs.types.sort_order

        out["Order"] = aws_sdk_workdocs.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> SearchSortResult:
    out: SearchSortResult = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        import aws_sdk_workdocs.types.order_by_field_type

        out["field"] = aws_sdk_workdocs.types.order_by_field_type.deserialize_json(
            data["Field"]
        )
    if "Order" in data:
        import aws_sdk_workdocs.types.sort_order

        out["order"] = aws_sdk_workdocs.types.sort_order.deserialize_json(data["Order"])
    return out

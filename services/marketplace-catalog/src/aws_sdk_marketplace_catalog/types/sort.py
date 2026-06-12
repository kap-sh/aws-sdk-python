"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Sort``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.sort_by
    import aws_sdk_marketplace_catalog.types.sort_order


class Sort(TypedDict):
    sort_by: NotRequired["aws_sdk_marketplace_catalog.types.sort_by.SortBy"]
    """<p>For <code>ListEntities</code>, supported attributes include <code>LastModifiedDate</code> (default) and <code>EntityId</code>. In addition to <code>LastModifiedDate</code> and <code>EntityId</code>, each <code>EntityType</code> might support additional fields.</p> <p>For <code>ListChangeSets</code>, supported attributes include <code>StartTime</code> and <code>EndTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>The sorting order. Can be <code>ASCENDING</code> or <code>DESCENDING</code>. The default value is <code>DESCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        out["SortBy"] = value["sort_by"]
    if "sort_order" in value:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["SortOrder"] = aws_sdk_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        out["sort_by"] = data["SortBy"]
    if "SortOrder" in data:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["sort_order"] = (
            aws_sdk_marketplace_catalog.types.sort_order.deserialize_json(
                data["SortOrder"]
            )
        )
    return out

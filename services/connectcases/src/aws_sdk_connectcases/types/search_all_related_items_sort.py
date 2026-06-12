"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsSort``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.order
    import aws_sdk_connectcases.types.search_all_related_items_sort_property


class SearchAllRelatedItemsSort(TypedDict):
    sort_property: "aws_sdk_connectcases.types.search_all_related_items_sort_property.SearchAllRelatedItemsSortProperty"
    """<p>Whether related items should be sorted in ascending or descending order. </p>"""
    sort_order: "aws_sdk_connectcases.types.order.Order"
    """<p>Whether related items should be sorted by association time or case ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsSort) -> dict:
    out: dict = {}
    out["sortProperty"] = value["sort_property"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsSort:
    out: SearchAllRelatedItemsSort = {}  # type: ignore[typeddict-item]
    if "sortProperty" in data:
        out["sort_property"] = data["sortProperty"]
    else:
        raise DeserializationError("SearchAllRelatedItemsSort.sort_property required")
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    else:
        raise DeserializationError("SearchAllRelatedItemsSort.sort_order required")
    return out

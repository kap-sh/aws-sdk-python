"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SortCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.order_by


class SortCriteria(TypedDict):
    attribute_name: NotRequired["str"]
    """<p>The name of the attribute to sort on.</p>"""
    order_by: NotRequired["aws_sdk_accessanalyzer.types.order_by.OrderBy"]
    """<p>The sort order, ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "order_by" in value:
        out["orderBy"] = value["order_by"]
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        out["attribute_name"] = data["attributeName"]
    if "orderBy" in data:
        out["order_by"] = data["orderBy"]
    return out

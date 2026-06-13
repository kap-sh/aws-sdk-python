"""Generated from Smithy shape ``com.amazonaws.datazone#SearchSort``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute
    import aws_sdk_datazone.types.sort_order


class SearchSort(TypedDict):
    attribute: "aws_sdk_datazone.types.attribute.Attribute"
    """<p>The attribute detail of the way to sort search results.</p>"""
    order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>The order detail of the wya to sort search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSort) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    if "order" in value:
        import aws_sdk_datazone.types.sort_order

        out["order"] = aws_sdk_datazone.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> SearchSort:
    out: SearchSort = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        out["attribute"] = data["attribute"]
    else:
        raise DeserializationError("SearchSort.attribute required")
    if "order" in data:
        import aws_sdk_datazone.types.sort_order

        out["order"] = aws_sdk_datazone.types.sort_order.deserialize_json(data["order"])
    return out

"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute


class SearchInItem(TypedDict):
    attribute: "aws_sdk_datazone.types.attribute.Attribute"
    """<p>The search attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchInItem) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    return out


def deserialize_json(data: dict) -> SearchInItem:
    out: SearchInItem = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        out["attribute"] = data["attribute"]
    else:
        raise DeserializationError("SearchInItem.attribute required")
    return out

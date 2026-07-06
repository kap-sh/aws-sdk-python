"""Generated from Smithy shape ``com.amazonaws.controlcatalog#FrameworkMappingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.framework_item
    import aws_sdk_controlcatalog.types.framework_name


class FrameworkMappingDetails(TypedDict, closed=True):
    name: "aws_sdk_controlcatalog.types.framework_name.FrameworkName"
    """<p>The name of the compliance framework that the control maps to.</p>"""
    item: "aws_sdk_controlcatalog.types.framework_item.FrameworkItem"
    """<p>The specific item or requirement within the framework that the control maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMappingDetails) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Item"] = value["item"]
    return out


def deserialize_json(data: dict) -> FrameworkMappingDetails:
    out: FrameworkMappingDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FrameworkMappingDetails.name required")
    if "Item" in data:
        out["item"] = data["Item"]
    else:
        raise DeserializationError("FrameworkMappingDetails.item required")
    return out

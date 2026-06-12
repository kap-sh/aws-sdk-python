"""Generated from Smithy shape ``com.amazonaws.notifications#Dimension``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_notifications.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.text_part_reference

class Dimension(TypedDict):
    name: "aws_sdk_notifications.types.text_part_reference.TextPartReference"
    """<p>The name of the dimension</p>"""
    value: "aws_sdk_notifications.types.text_part_reference.TextPartReference"
    """<p>The value of the dimension.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Dimension.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Dimension.value required")
    return out
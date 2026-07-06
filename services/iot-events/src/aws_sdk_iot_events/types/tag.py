"""Generated from Smithy shape ``com.amazonaws.iotevents#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.tag_key
    import aws_sdk_iot_events.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_iot_events.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: "aws_sdk_iot_events.types.tag_value.TagValue"
    """<p>The tag's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out

"""Generated from Smithy shape ``com.amazonaws.pipes#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.tag_key
    import aws_sdk_pipes.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_pipes.types.tag_key.TagKey"
    """<p>A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.</p>"""
    value: "aws_sdk_pipes.types.tag_value.TagValue"
    """<p>The value for the specified tag key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out

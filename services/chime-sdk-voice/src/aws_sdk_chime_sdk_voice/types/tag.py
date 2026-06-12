"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.tag_key
    import aws_sdk_chime_sdk_voice.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_chime_sdk_voice.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: "aws_sdk_chime_sdk_voice.types.tag_value.TagValue"
    """<p>The tag's value.</p>"""


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

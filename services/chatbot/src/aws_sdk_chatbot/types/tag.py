"""Generated from Smithy shape ``com.amazonaws.chatbot#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.tag_key
    import aws_sdk_chatbot.types.tag_value


class Tag(TypedDict, closed=True):
    tag_key: "aws_sdk_chatbot.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    tag_value: "aws_sdk_chatbot.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    out["TagValue"] = value["tag_value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("Tag.tag_key required")
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    else:
        raise DeserializationError("Tag.tag_value required")
    return out

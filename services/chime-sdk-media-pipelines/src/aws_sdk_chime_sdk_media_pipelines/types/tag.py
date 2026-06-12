"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.tag_key
    import aws_sdk_chime_sdk_media_pipelines.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_chime_sdk_media_pipelines.types.tag_key.TagKey"
    """<p>The key half of a tag.</p>"""
    value: "aws_sdk_chime_sdk_media_pipelines.types.tag_value.TagValue"
    """<p>The value half of a tag.</p>"""


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

"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.tag_key
    import capo_kinesis_video.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_kinesis_video.types.tag_key.TagKey"
    """<p>The key of the tag that is associated with the specified signaling channel.</p>"""
    value: "capo_kinesis_video.types.tag_value.TagValue"
    """<p>The value of the tag that is associated with the specified signaling channel.</p>"""


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

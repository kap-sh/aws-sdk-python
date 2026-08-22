"""Generated from Smithy shape ``com.amazonaws.bedrock#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.tag_key
    import capo_bedrock.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_bedrock.types.tag_key.TagKey"
    """<p>Key for the tag.</p>"""
    value: "capo_bedrock.types.tag_value.TagValue"
    """<p>Value for the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out

"""Generated from Smithy shape ``com.amazonaws.efs#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.tag_key
    import capo_efs.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_efs.types.tag_key.TagKey"
    """<p>The tag key (String). The key can't start with <code>aws:</code>.</p>"""
    value: "capo_efs.types.tag_value.TagValue"
    """<p>The value of the tag key.</p>"""


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

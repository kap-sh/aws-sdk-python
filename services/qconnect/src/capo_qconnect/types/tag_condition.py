"""Generated from Smithy shape ``com.amazonaws.qconnect#TagCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.tag_key
    import capo_qconnect.types.tag_value


class TagCondition(TypedDict, closed=True):
    key: "capo_qconnect.types.tag_key.TagKey"
    """<p>The tag key in the tag condition.</p>"""
    value: NotRequired["capo_qconnect.types.tag_value.TagValue"]
    """<p>The tag value in the tag condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCondition) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagCondition:
    out: TagCondition = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TagCondition.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out

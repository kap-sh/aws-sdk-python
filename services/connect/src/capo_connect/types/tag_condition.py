"""Generated from Smithy shape ``com.amazonaws.connect#TagCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string


class TagCondition(TypedDict, closed=True):
    tag_key: NotRequired["capo_connect.types.string.String"]
    """<p>The tag key in the tag condition.</p>"""
    tag_value: NotRequired["capo_connect.types.string.String"]
    """<p>The tag value in the tag condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCondition) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    return out


def deserialize_json(data: dict) -> TagCondition:
    out: TagCondition = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    return out

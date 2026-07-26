"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.tag_key
    import capo_clouddirectory.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_clouddirectory.types.tag_key.TagKey"]
    """<p>The key that is associated with the tag.</p>"""
    value: NotRequired["capo_clouddirectory.types.tag_value.TagValue"]
    """<p>The value that is associated with the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out

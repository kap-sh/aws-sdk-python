"""Generated from Smithy shape ``com.amazonaws.connectcases#TagValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.search_tag_key
    import capo_connectcases.types.tag_value_string


class TagValue(TypedDict, closed=True):
    key: NotRequired["capo_connectcases.types.search_tag_key.SearchTagKey"]
    """<p>The tag key in the tag filter value.</p>"""
    value: NotRequired["capo_connectcases.types.tag_value_string.TagValueString"]
    """<p>The tag value in the tag filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagValue) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagValue:
    out: TagValue = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out

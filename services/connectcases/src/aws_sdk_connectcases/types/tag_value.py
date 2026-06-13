"""Generated from Smithy shape ``com.amazonaws.connectcases#TagValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.search_tag_key
    import aws_sdk_connectcases.types.tag_value_string


class TagValue(TypedDict):
    key: NotRequired["aws_sdk_connectcases.types.search_tag_key.SearchTagKey"]
    """<p>The tag key in the tag filter value.</p>"""
    value: NotRequired["aws_sdk_connectcases.types.tag_value_string.TagValueString"]
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

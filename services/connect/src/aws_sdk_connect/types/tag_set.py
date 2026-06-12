"""Generated from Smithy shape ``com.amazonaws.connect#TagSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_key
    import aws_sdk_connect.types.tag_value


class TagSet(TypedDict):
    key: NotRequired["aws_sdk_connect.types.tag_key.TagKey"]
    """<p>The tag key in the TagSet.</p>"""
    value: NotRequired["aws_sdk_connect.types.tag_value.TagValue"]
    """<p>The tag value in the tagSet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagSet) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagSet:
    out: TagSet = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out

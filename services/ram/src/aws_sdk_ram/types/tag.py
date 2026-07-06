"""Generated from Smithy shape ``com.amazonaws.ram#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.tag_key
    import aws_sdk_ram.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_ram.types.tag_key.TagKey"]
    """<p>The key, or name, attached to the tag. Every tag must have a key. Key names are case sensitive.</p>"""
    value: NotRequired["aws_sdk_ram.types.tag_value.TagValue"]
    """<p>The string value attached to the tag. The value can be an empty string. Key values are case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.tag_key
    import aws_sdk_iot.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_iot.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: NotRequired["aws_sdk_iot.types.tag_value.TagValue"]
    """<p>The tag's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
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
    return out

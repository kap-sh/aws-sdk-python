"""Generated from Smithy shape ``com.amazonaws.qconnect#TagCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.tag_key
    import aws_sdk_qconnect.types.tag_value


class TagCondition(TypedDict):
    key: "aws_sdk_qconnect.types.tag_key.TagKey"
    """<p>The tag key in the tag condition.</p>"""
    value: NotRequired["aws_sdk_qconnect.types.tag_value.TagValue"]
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

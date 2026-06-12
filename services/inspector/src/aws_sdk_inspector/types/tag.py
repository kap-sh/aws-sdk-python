"""Generated from Smithy shape ``com.amazonaws.inspector#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.tag_key
    import aws_sdk_inspector.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_inspector.types.tag_key.TagKey"
    """<p>A tag key.</p>"""
    value: NotRequired["aws_sdk_inspector.types.tag_value.TagValue"]
    """<p>A value assigned to a tag key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroupTag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.tag_key
    import aws_sdk_inspector.types.tag_value


class ResourceGroupTag(TypedDict):
    key: "aws_sdk_inspector.types.tag_key.TagKey"
    """<p>A tag key.</p>"""
    value: NotRequired["aws_sdk_inspector.types.tag_value.TagValue"]
    """<p>The value assigned to a tag key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroupTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceGroupTag:
    out: ResourceGroupTag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceGroupTag.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out

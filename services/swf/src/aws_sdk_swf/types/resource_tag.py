"""Generated from Smithy shape ``com.amazonaws.swf#ResourceTag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.resource_tag_key
    import aws_sdk_swf.types.resource_tag_value


class ResourceTag(TypedDict):
    key: "aws_sdk_swf.types.resource_tag_key.ResourceTagKey"
    """<p>The key of a tag.</p>"""
    value: NotRequired["aws_sdk_swf.types.resource_tag_value.ResourceTagValue"]
    """<p>The value of a tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out

"""Generated from Smithy shape ``com.amazonaws.appintegrations#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_appintegrations.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.tag_map

class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_appintegrations.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_appintegrations.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_appintegrations.types.tag_map
    out["tags"] = aws_sdk_appintegrations.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_appintegrations.types.tag_map
        out["tags"] = aws_sdk_appintegrations.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
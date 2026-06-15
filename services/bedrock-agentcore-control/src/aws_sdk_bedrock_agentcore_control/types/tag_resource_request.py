"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
    """<p>The tags to add to the resource. A tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.tags_map

    out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

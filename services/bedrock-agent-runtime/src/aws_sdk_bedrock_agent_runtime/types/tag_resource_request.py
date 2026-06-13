"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn
    import aws_sdk_bedrock_agent_runtime.types.tags_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "aws_sdk_bedrock_agent_runtime.types.tags_map.TagsMap"
    """<p>An object containing key-value pairs that define the tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.tags_map

    out["tags"] = aws_sdk_bedrock_agent_runtime.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_bedrock_agent_runtime.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent_runtime.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

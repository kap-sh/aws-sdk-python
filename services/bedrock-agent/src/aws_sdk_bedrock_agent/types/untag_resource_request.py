"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.tag_key_list
    import aws_sdk_bedrock_agent.types.taggable_resources_arn


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "aws_sdk_bedrock_agent.types.tag_key_list.TagKeyList"
    """<p>A list of keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.tag_key_list
    import capo_bedrock_agentcore_control.types.taggable_resources_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>"""
    tag_keys: "capo_bedrock_agentcore_control.types.tag_key_list.TagKeyList"
    """<p>The tag keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn

class GetResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to retrieve the resource policy.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
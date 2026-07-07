"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import aws_sdk_bedrock_agentcore_control.types.resource_policy_body


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to create or update the resource policy.</p>"""
    policy: "aws_sdk_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody"
    """<p>The resource policy to create or update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out

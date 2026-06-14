"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class DeletePolicyRequest(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.</p>"""
    policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyRequest:
    out: DeletePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

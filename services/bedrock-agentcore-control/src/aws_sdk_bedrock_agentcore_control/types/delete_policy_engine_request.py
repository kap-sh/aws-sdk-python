"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePolicyEngineRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id

class DeletePolicyEngineRequest(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine to be deleted. This must be a valid policy engine ID that exists within the account.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyEngineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyEngineRequest:
    out: DeletePolicyEngineRequest = {}  # type: ignore[typeddict-item]
    return out
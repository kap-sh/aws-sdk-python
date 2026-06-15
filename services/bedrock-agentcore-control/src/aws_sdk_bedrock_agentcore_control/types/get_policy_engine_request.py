"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyEngineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class GetPolicyEngineRequest(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine to be retrieved. This must be a valid policy engine ID that exists within the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyEngineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyEngineRequest:
    out: GetPolicyEngineRequest = {}  # type: ignore[typeddict-item]
    return out

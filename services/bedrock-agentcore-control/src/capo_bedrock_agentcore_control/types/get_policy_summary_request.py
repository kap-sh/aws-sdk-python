"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicySummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_id


class GetPolicySummaryRequest(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages the policy to retrieve the summary for.</p>"""
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy to retrieve the summary for. This must be a valid policy ID that exists within the specified policy engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicySummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicySummaryRequest:
    out: GetPolicySummaryRequest = {}  # type: ignore[typeddict-item]
    return out

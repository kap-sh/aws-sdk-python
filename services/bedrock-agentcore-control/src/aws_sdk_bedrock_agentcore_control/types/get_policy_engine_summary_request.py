"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyEngineSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class GetPolicyEngineSummaryRequest(TypedDict, closed=True):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine to retrieve the summary for. This must be a valid policy engine ID that exists within the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyEngineSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyEngineSummaryRequest:
    out: GetPolicyEngineSummaryRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyGenerationSummaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class GetPolicyGenerationSummaryRequest(TypedDict):
    policy_generation_id: (
        "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier of the policy generation request to retrieve the summary for.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine associated with the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyGenerationSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyGenerationSummaryRequest:
    out: GetPolicyGenerationSummaryRequest = {}  # type: ignore[typeddict-item]
    return out

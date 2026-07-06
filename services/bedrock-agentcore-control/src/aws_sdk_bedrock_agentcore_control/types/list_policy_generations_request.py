"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class ListPolicyGenerationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A pagination token for retrieving additional policy generations when results are paginated.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of policy generations to return in a single response.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine whose policy generations to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsRequest:
    out: ListPolicyGenerationsRequest = {}  # type: ignore[typeddict-item]
    return out

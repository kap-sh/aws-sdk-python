"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class ListPoliciesRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    r"""<p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html\">ListPolicies</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of policies to return in a single response. If not specified, the default is 10 policies per page, with a maximum of 100 per page.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine whose policies to retrieve.</p>"""
    target_resource_scope: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    ]
    """<p>Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPoliciesRequest:
    out: ListPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out

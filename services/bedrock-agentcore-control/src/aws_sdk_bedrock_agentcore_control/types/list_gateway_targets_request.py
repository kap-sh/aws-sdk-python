"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.target_max_results
    import aws_sdk_bedrock_agentcore_control.types.target_next_token


class ListGatewayTargetsRequest(TypedDict):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to list targets for.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_max_results.TargetMaxResults"
    ]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.target_next_token.TargetNextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayTargetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGatewayTargetsRequest:
    out: ListGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
    return out

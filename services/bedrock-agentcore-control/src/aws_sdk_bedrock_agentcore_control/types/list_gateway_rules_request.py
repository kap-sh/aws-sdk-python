"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_max_results
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_next_token


class ListGatewayRulesRequest(TypedDict, closed=True):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to list rules for.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_max_results.GatewayRuleMaxResults"
    ]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
    ]
    """<p>The pagination token from a previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGatewayRulesRequest:
    out: ListGatewayRulesRequest = {}  # type: ignore[typeddict-item]
    return out

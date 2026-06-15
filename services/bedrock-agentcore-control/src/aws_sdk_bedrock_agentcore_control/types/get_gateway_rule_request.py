"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_id


class GetGatewayRuleRequest(TypedDict):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway containing the rule.</p>"""
    rule_id: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the rule to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayRuleRequest:
    out: GetGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rule_id


class GetGatewayRuleRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway containing the rule.</p>"""
    rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the rule to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayRuleRequest:
    out: GetGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    return out

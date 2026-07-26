"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rule_detail

GatewayRules: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_rule_detail.GatewayRuleDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRules) -> list:
    import capo_bedrock_agentcore_control.types.gateway_rule_detail

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_rule_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GatewayRules:
    import capo_bedrock_agentcore_control.types.gateway_rule_detail

    out: GatewayRules = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_rule_detail.deserialize_json(
                item
            )
        )
    return out

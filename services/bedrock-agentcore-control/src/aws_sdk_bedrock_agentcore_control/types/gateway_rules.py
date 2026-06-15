"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail

GatewayRules: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail.GatewayRuleDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRules) -> list:
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GatewayRules:
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail

    out: GatewayRules = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.gateway_rule_detail.deserialize_json(
                item
            )
        )
    return out

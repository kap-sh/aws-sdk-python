"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptionPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_interception_point

GatewayInterceptionPoints: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_interception_point.GatewayInterceptionPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayInterceptionPoints) -> list:
    import capo_bedrock_agentcore_control.types.gateway_interception_point

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_interception_point.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GatewayInterceptionPoints:
    import capo_bedrock_agentcore_control.types.gateway_interception_point

    out: GatewayInterceptionPoints = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_interception_point.deserialize_json(
                item
            )
        )
    return out

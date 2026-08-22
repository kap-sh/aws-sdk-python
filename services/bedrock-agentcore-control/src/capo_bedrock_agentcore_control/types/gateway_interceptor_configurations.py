"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptorConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configuration

GatewayInterceptorConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_interceptor_configuration.GatewayInterceptorConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayInterceptorConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_interceptor_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GatewayInterceptorConfigurations:
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configuration

    out: GatewayInterceptorConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.gateway_interceptor_configuration.deserialize_json(
                item
            )
        )
    return out

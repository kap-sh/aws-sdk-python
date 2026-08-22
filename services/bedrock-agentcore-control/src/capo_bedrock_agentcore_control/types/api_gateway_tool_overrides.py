"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_override

ApiGatewayToolOverrides: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.api_gateway_tool_override.ApiGatewayToolOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolOverrides) -> list:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_override

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.api_gateway_tool_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApiGatewayToolOverrides:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_override

    out: ApiGatewayToolOverrides = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.api_gateway_tool_override.deserialize_json(
                item
            )
        )
    return out

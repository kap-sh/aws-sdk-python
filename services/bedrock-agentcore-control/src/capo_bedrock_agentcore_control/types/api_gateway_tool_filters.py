"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_filter

ApiGatewayToolFilters: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.api_gateway_tool_filter.ApiGatewayToolFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolFilters) -> list:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.api_gateway_tool_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApiGatewayToolFilters:
    import capo_bedrock_agentcore_control.types.api_gateway_tool_filter

    out: ApiGatewayToolFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.api_gateway_tool_filter.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolFilters``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter

ApiGatewayToolFilters: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter.ApiGatewayToolFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolFilters) -> list:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApiGatewayToolFilters:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter
    out: ApiGatewayToolFilters = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_filter.deserialize_json(item))
    return out
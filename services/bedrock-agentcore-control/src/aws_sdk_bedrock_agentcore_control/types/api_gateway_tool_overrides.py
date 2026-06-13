"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolOverrides``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override

ApiGatewayToolOverrides: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override.ApiGatewayToolOverride"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolOverrides) -> list:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApiGatewayToolOverrides:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override
    out: ApiGatewayToolOverrides = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.api_gateway_tool_override.deserialize_json(item))
    return out
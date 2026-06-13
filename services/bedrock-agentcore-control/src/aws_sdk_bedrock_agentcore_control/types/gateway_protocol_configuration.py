"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration

class _GatewayProtocolConfiguration_mcp(TypedDict):
    mcp: "aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration.MCPGatewayConfiguration"

GatewayProtocolConfiguration: TypeAlias = _GatewayProtocolConfiguration_mcp

# --- restJson1 ser/de ---
def serialize_json(value: GatewayProtocolConfiguration) -> dict:
    if "mcp" in value:
        import aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration
        return {"mcp": aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration.serialize_json(value["mcp"])}
    else:
        raise SerializationError("GatewayProtocolConfiguration: no variant present")


def deserialize_json(data: dict) -> GatewayProtocolConfiguration:
    if "mcp" in data:
        import aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration
        return {"mcp": aws_sdk_bedrock_agentcore_control.types.mcp_gateway_configuration.deserialize_json(data["mcp"])}
    else:
        raise DeserializationError("GatewayProtocolConfiguration: no recognized variant key")
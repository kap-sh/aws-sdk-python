"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpDescriptor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.server_definition
    import aws_sdk_bedrock_agentcore_control.types.tools_definition


class McpDescriptor(TypedDict):
    server: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.server_definition.ServerDefinition"
    ]
    """<p>The MCP server definition, containing the server configuration and schema as defined by the MCP protocol specification.</p>"""
    tools: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.tools_definition.ToolsDefinition"
    ]
    """<p>The MCP tools definition, containing the tools available on the MCP server as defined by the MCP protocol specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpDescriptor) -> dict:
    out: dict = {}
    if "server" in value:
        import aws_sdk_bedrock_agentcore_control.types.server_definition

        out["server"] = (
            aws_sdk_bedrock_agentcore_control.types.server_definition.serialize_json(
                value["server"]
            )
        )
    if "tools" in value:
        import aws_sdk_bedrock_agentcore_control.types.tools_definition

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.tools_definition.serialize_json(
                value["tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> McpDescriptor:
    out: McpDescriptor = {}  # type: ignore[typeddict-item]
    if "server" in data:
        import aws_sdk_bedrock_agentcore_control.types.server_definition

        out["server"] = (
            aws_sdk_bedrock_agentcore_control.types.server_definition.deserialize_json(
                data["server"]
            )
        )
    if "tools" in data:
        import aws_sdk_bedrock_agentcore_control.types.tools_definition

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.tools_definition.deserialize_json(
                data["tools"]
            )
        )
    return out

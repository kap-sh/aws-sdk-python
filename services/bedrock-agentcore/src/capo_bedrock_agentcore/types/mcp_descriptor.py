"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#McpDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.server_definition
    import capo_bedrock_agentcore.types.tools_definition


class McpDescriptor(TypedDict, closed=True):
    server: "capo_bedrock_agentcore.types.server_definition.ServerDefinition"
    """<p> The MCP server definition that describes the server configuration.</p>"""
    tools: "capo_bedrock_agentcore.types.tools_definition.ToolsDefinition"
    """<p> The MCP tools definition that describes the available tools.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpDescriptor) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.server_definition

    out["server"] = capo_bedrock_agentcore.types.server_definition.serialize_json(
        value["server"]
    )
    import capo_bedrock_agentcore.types.tools_definition

    out["tools"] = capo_bedrock_agentcore.types.tools_definition.serialize_json(
        value["tools"]
    )
    return out


def deserialize_json(data: dict) -> McpDescriptor:
    out: McpDescriptor = {}  # type: ignore[typeddict-item]
    if "server" in data:
        import capo_bedrock_agentcore.types.server_definition

        out["server"] = capo_bedrock_agentcore.types.server_definition.deserialize_json(
            data["server"]
        )
    else:
        raise DeserializationError("McpDescriptor.server required")
    if "tools" in data:
        import capo_bedrock_agentcore.types.tools_definition

        out["tools"] = capo_bedrock_agentcore.types.tools_definition.deserialize_json(
            data["tools"]
        )
    else:
        raise DeserializationError("McpDescriptor.tools required")
    return out

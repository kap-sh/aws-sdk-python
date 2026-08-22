"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedMcpDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.updated_server_definition
    import capo_bedrock_agentcore_control.types.updated_tools_definition


class UpdatedMcpDescriptorFields(TypedDict, closed=True):
    server: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_server_definition.UpdatedServerDefinition"
    ]
    """<p>The updated server definition for the MCP descriptor.</p>"""
    tools: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_tools_definition.UpdatedToolsDefinition"
    ]
    """<p>The updated tools definition for the MCP descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpDescriptorFields) -> dict:
    out: dict = {}
    if "server" in value:
        import capo_bedrock_agentcore_control.types.updated_server_definition

        out["server"] = (
            capo_bedrock_agentcore_control.types.updated_server_definition.serialize_json(
                value["server"]
            )
        )
    if "tools" in value:
        import capo_bedrock_agentcore_control.types.updated_tools_definition

        out["tools"] = (
            capo_bedrock_agentcore_control.types.updated_tools_definition.serialize_json(
                value["tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedMcpDescriptorFields:
    out: UpdatedMcpDescriptorFields = {}  # type: ignore[typeddict-item]
    if data.get("server") is not None:
        import capo_bedrock_agentcore_control.types.updated_server_definition

        out["server"] = (
            capo_bedrock_agentcore_control.types.updated_server_definition.deserialize_json(
                data["server"]
            )
        )
    if data.get("tools") is not None:
        import capo_bedrock_agentcore_control.types.updated_tools_definition

        out["tools"] = (
            capo_bedrock_agentcore_control.types.updated_tools_definition.deserialize_json(
                data["tools"]
            )
        )
    return out

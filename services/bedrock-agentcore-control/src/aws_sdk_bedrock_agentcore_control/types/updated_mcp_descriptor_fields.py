"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedMcpDescriptorFields``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.updated_server_definition
    import aws_sdk_bedrock_agentcore_control.types.updated_tools_definition


class UpdatedMcpDescriptorFields(TypedDict):
    server: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_server_definition.UpdatedServerDefinition"
    ]
    """<p>The updated server definition for the MCP descriptor.</p>"""
    tools: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_tools_definition.UpdatedToolsDefinition"
    ]
    """<p>The updated tools definition for the MCP descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpDescriptorFields) -> dict:
    out: dict = {}
    if "server" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_server_definition

        out["server"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_server_definition.serialize_json(
                value["server"]
            )
        )
    if "tools" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_tools_definition

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_tools_definition.serialize_json(
                value["tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedMcpDescriptorFields:
    out: UpdatedMcpDescriptorFields = {}  # type: ignore[typeddict-item]
    if "server" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_server_definition

        out["server"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_server_definition.deserialize_json(
                data["server"]
            )
        )
    if "tools" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_tools_definition

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_tools_definition.deserialize_json(
                data["tools"]
            )
        )
    return out

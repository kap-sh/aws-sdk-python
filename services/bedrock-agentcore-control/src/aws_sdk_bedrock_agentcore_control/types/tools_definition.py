"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolsDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.inline_content
    import aws_sdk_bedrock_agentcore_control.types.schema_version


class ToolsDefinition(TypedDict):
    protocol_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_version.SchemaVersion"
    ]
    """<p>The protocol version of the tools definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.inline_content.InlineContent"
    ]
    """<p>The JSON content containing the MCP tools definition, conforming to the MCP protocol specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolsDefinition) -> dict:
    out: dict = {}
    if "protocol_version" in value:
        out["protocolVersion"] = value["protocol_version"]
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> ToolsDefinition:
    out: ToolsDefinition = {}  # type: ignore[typeddict-item]
    if "protocolVersion" in data:
        out["protocol_version"] = data["protocolVersion"]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out

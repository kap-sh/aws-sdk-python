"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolsDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.inline_content
    import capo_bedrock_agentcore.types.schema_version


class ToolsDefinition(TypedDict, closed=True):
    protocol_version: NotRequired[
        "capo_bedrock_agentcore.types.schema_version.SchemaVersion"
    ]
    """<p> The MCP protocol version that the tools conform to. This differs from the <code>schemaVersion</code> field in the server definition, which identifies the server configuration schema format.</p>"""
    inline_content: NotRequired[
        "capo_bedrock_agentcore.types.inline_content.InlineContent"
    ]
    """<p> The inline content of the tools definition.</p>"""


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
    if data.get("protocolVersion") is not None:
        out["protocol_version"] = data["protocolVersion"]
    if data.get("inlineContent") is not None:
        out["inline_content"] = data["inlineContent"]
    return out

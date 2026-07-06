"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.inline_content
    import aws_sdk_bedrock_agentcore_control.types.schema_version


class ServerDefinition(TypedDict, closed=True):
    schema_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_version.SchemaVersion"
    ]
    """<p>The schema version of the server definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.inline_content.InlineContent"
    ]
    """<p>The JSON content containing the MCP server definition, conforming to the MCP protocol specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerDefinition) -> dict:
    out: dict = {}
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> ServerDefinition:
    out: ServerDefinition = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out

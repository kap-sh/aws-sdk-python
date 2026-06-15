"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ServerDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.inline_content
    import aws_sdk_bedrock_agentcore.types.schema_version


class ServerDefinition(TypedDict):
    schema_version: NotRequired[
        "aws_sdk_bedrock_agentcore.types.schema_version.SchemaVersion"
    ]
    """<p> The schema version of the MCP server configuration. The schema version identifies the format of the server definition content.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agentcore.types.inline_content.InlineContent"
    ]
    """<p> The inline content of the server definition.</p>"""


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

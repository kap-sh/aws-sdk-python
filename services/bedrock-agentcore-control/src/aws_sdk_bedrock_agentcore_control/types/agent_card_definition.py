"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentCardDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.inline_content
    import aws_sdk_bedrock_agentcore_control.types.schema_version


class AgentCardDefinition(TypedDict):
    schema_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_version.SchemaVersion"
    ]
    """<p>The schema version of the agent card based on the A2A protocol specification.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.inline_content.InlineContent"
    ]
    """<p>The JSON content containing the A2A agent card definition, conforming to the A2A protocol specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCardDefinition) -> dict:
    out: dict = {}
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> AgentCardDefinition:
    out: AgentCardDefinition = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out

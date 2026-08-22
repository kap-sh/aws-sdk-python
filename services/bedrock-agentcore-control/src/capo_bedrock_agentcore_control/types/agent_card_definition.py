"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentCardDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inline_content
    import capo_bedrock_agentcore_control.types.schema_version


class AgentCardDefinition(TypedDict, closed=True):
    schema_version: NotRequired[
        "capo_bedrock_agentcore_control.types.schema_version.SchemaVersion"
    ]
    """<p>The schema version of the agent card based on the A2A protocol specification.</p>"""
    inline_content: NotRequired[
        "capo_bedrock_agentcore_control.types.inline_content.InlineContent"
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
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    if data.get("inlineContent") is not None:
        out["inline_content"] = data["inlineContent"]
    return out

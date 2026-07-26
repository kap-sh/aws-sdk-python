"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SkillDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.inline_content
    import capo_bedrock_agentcore.types.schema_version


class SkillDefinition(TypedDict, closed=True):
    schema_version: NotRequired[
        "capo_bedrock_agentcore.types.schema_version.SchemaVersion"
    ]
    """<p> The schema version of the skill definition. If you don't specify a version, the service detects it automatically.</p>"""
    inline_content: NotRequired[
        "capo_bedrock_agentcore.types.inline_content.InlineContent"
    ]
    """<p> The inline content of the skill definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SkillDefinition) -> dict:
    out: dict = {}
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> SkillDefinition:
    out: SkillDefinition = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out

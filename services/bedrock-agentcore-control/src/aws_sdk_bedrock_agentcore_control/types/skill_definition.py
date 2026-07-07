"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SkillDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.inline_content
    import aws_sdk_bedrock_agentcore_control.types.schema_version


class SkillDefinition(TypedDict, closed=True):
    schema_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_version.SchemaVersion"
    ]
    """<p>The version of the skill definition schema.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.inline_content.InlineContent"
    ]
    """<p>The JSON content containing the structured skill definition.</p>"""


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

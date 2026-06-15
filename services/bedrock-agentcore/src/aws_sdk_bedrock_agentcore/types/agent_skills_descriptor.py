"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentSkillsDescriptor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.skill_definition
    import aws_sdk_bedrock_agentcore.types.skill_md_definition


class AgentSkillsDescriptor(TypedDict):
    skill_md: "aws_sdk_bedrock_agentcore.types.skill_md_definition.SkillMdDefinition"
    """<p> The skill description in markdown format.</p>"""
    skill_definition: NotRequired[
        "aws_sdk_bedrock_agentcore.types.skill_definition.SkillDefinition"
    ]
    """<p> The structured skill definition with a schema version and content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSkillsDescriptor) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.skill_md_definition

    out["skillMd"] = aws_sdk_bedrock_agentcore.types.skill_md_definition.serialize_json(
        value["skill_md"]
    )
    if "skill_definition" in value:
        import aws_sdk_bedrock_agentcore.types.skill_definition

        out["skillDefinition"] = (
            aws_sdk_bedrock_agentcore.types.skill_definition.serialize_json(
                value["skill_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSkillsDescriptor:
    out: AgentSkillsDescriptor = {}  # type: ignore[typeddict-item]
    if "skillMd" in data:
        import aws_sdk_bedrock_agentcore.types.skill_md_definition

        out["skill_md"] = (
            aws_sdk_bedrock_agentcore.types.skill_md_definition.deserialize_json(
                data["skillMd"]
            )
        )
    else:
        raise DeserializationError("AgentSkillsDescriptor.skill_md required")
    if "skillDefinition" in data:
        import aws_sdk_bedrock_agentcore.types.skill_definition

        out["skill_definition"] = (
            aws_sdk_bedrock_agentcore.types.skill_definition.deserialize_json(
                data["skillDefinition"]
            )
        )
    return out

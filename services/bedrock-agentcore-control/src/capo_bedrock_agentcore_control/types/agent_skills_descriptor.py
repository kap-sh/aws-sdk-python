"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentSkillsDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.skill_definition
    import capo_bedrock_agentcore_control.types.skill_md_definition


class AgentSkillsDescriptor(TypedDict, closed=True):
    skill_md: NotRequired[
        "capo_bedrock_agentcore_control.types.skill_md_definition.SkillMdDefinition"
    ]
    """<p>The optional skill markdown definition describing the agent's skills in a human-readable format.</p>"""
    skill_definition: NotRequired[
        "capo_bedrock_agentcore_control.types.skill_definition.SkillDefinition"
    ]
    """<p>The structured skill definition with schema version and content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSkillsDescriptor) -> dict:
    out: dict = {}
    if "skill_md" in value:
        import capo_bedrock_agentcore_control.types.skill_md_definition

        out["skillMd"] = (
            capo_bedrock_agentcore_control.types.skill_md_definition.serialize_json(
                value["skill_md"]
            )
        )
    if "skill_definition" in value:
        import capo_bedrock_agentcore_control.types.skill_definition

        out["skillDefinition"] = (
            capo_bedrock_agentcore_control.types.skill_definition.serialize_json(
                value["skill_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSkillsDescriptor:
    out: AgentSkillsDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("skillMd") is not None:
        import capo_bedrock_agentcore_control.types.skill_md_definition

        out["skill_md"] = (
            capo_bedrock_agentcore_control.types.skill_md_definition.deserialize_json(
                data["skillMd"]
            )
        )
    if data.get("skillDefinition") is not None:
        import capo_bedrock_agentcore_control.types.skill_definition

        out["skill_definition"] = (
            capo_bedrock_agentcore_control.types.skill_definition.deserialize_json(
                data["skillDefinition"]
            )
        )
    return out

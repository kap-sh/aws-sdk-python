"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedAgentSkillsDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields


class UpdatedAgentSkillsDescriptor(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields.UpdatedAgentSkillsDescriptorFields"
    ]
    """<p>The updated agent skills descriptor fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgentSkillsDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgentSkillsDescriptor:
    out: UpdatedAgentSkillsDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.updated_agent_skills_descriptor_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out

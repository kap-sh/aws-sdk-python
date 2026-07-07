"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedSkillMdDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.skill_md_definition


class UpdatedSkillMdDefinition(TypedDict, closed=True):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.skill_md_definition.SkillMdDefinition"
    ]
    """<p>The updated skill markdown definition value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedSkillMdDefinition) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.skill_md_definition

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.skill_md_definition.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedSkillMdDefinition:
    out: UpdatedSkillMdDefinition = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.skill_md_definition

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.skill_md_definition.deserialize_json(
                data["optionalValue"]
            )
        )
    return out

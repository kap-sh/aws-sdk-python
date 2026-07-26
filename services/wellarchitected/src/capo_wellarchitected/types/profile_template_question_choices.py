"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileTemplateQuestionChoices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_template_choice

ProfileTemplateQuestionChoices: TypeAlias = list[
    "capo_wellarchitected.types.profile_template_choice.ProfileTemplateChoice"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTemplateQuestionChoices) -> list:
    import capo_wellarchitected.types.profile_template_choice

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.profile_template_choice.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileTemplateQuestionChoices:
    import capo_wellarchitected.types.profile_template_choice

    out: ProfileTemplateQuestionChoices = []
    for item in data:
        out.append(
            capo_wellarchitected.types.profile_template_choice.deserialize_json(item)
        )
    return out

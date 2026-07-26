"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TemplateQuestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_template_question

TemplateQuestions: TypeAlias = list[
    "capo_wellarchitected.types.profile_template_question.ProfileTemplateQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateQuestions) -> list:
    import capo_wellarchitected.types.profile_template_question

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.profile_template_question.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateQuestions:
    import capo_wellarchitected.types.profile_template_question

    out: TemplateQuestions = []
    for item in data:
        out.append(
            capo_wellarchitected.types.profile_template_question.deserialize_json(item)
        )
    return out

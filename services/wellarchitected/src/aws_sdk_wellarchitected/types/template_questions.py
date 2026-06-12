"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TemplateQuestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_template_question

TemplateQuestions: TypeAlias = list[
    "aws_sdk_wellarchitected.types.profile_template_question.ProfileTemplateQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateQuestions) -> list:
    import aws_sdk_wellarchitected.types.profile_template_question

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.profile_template_question.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateQuestions:
    import aws_sdk_wellarchitected.types.profile_template_question

    out: TemplateQuestions = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.profile_template_question.deserialize_json(
                item
            )
        )
    return out

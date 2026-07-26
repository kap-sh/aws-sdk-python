"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_numeric_question_option

EvaluationFormNumericQuestionOptionList: TypeAlias = list[
    "capo_connect.types.evaluation_form_numeric_question_option.EvaluationFormNumericQuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionOptionList) -> list:
    import capo_connect.types.evaluation_form_numeric_question_option

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_numeric_question_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormNumericQuestionOptionList:
    import capo_connect.types.evaluation_form_numeric_question_option

    out: EvaluationFormNumericQuestionOptionList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_numeric_question_option.deserialize_json(
                item
            )
        )
    return out

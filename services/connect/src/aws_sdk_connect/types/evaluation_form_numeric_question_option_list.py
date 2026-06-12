"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_numeric_question_option

EvaluationFormNumericQuestionOptionList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_numeric_question_option.EvaluationFormNumericQuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionOptionList) -> list:
    import aws_sdk_connect.types.evaluation_form_numeric_question_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_numeric_question_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormNumericQuestionOptionList:
    import aws_sdk_connect.types.evaluation_form_numeric_question_option

    out: EvaluationFormNumericQuestionOptionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_numeric_question_option.deserialize_json(
                item
            )
        )
    return out

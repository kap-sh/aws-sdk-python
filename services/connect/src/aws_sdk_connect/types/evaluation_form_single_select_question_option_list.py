"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_single_select_question_option

EvaluationFormSingleSelectQuestionOptionList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_single_select_question_option.EvaluationFormSingleSelectQuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionOptionList) -> list:
    import aws_sdk_connect.types.evaluation_form_single_select_question_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_single_select_question_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormSingleSelectQuestionOptionList:
    import aws_sdk_connect.types.evaluation_form_single_select_question_option

    out: EvaluationFormSingleSelectQuestionOptionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_single_select_question_option.deserialize_json(
                item
            )
        )
    return out

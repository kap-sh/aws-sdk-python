"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option

EvaluationFormSingleSelectQuestionAutomationOptionList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_single_select_question_automation_option.EvaluationFormSingleSelectQuestionAutomationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: EvaluationFormSingleSelectQuestionAutomationOptionList,
) -> list:
    import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_single_select_question_automation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> EvaluationFormSingleSelectQuestionAutomationOptionList:
    import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option

    out: EvaluationFormSingleSelectQuestionAutomationOptionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_single_select_question_automation_option.deserialize_json(
                item
            )
        )
    return out

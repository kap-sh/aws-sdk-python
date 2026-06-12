"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option

EvaluationFormMultiSelectQuestionAutomationOptionList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option.EvaluationFormMultiSelectQuestionAutomationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: EvaluationFormMultiSelectQuestionAutomationOptionList,
) -> list:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> EvaluationFormMultiSelectQuestionAutomationOptionList:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option

    out: EvaluationFormMultiSelectQuestionAutomationOptionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option.deserialize_json(
                item
            )
        )
    return out

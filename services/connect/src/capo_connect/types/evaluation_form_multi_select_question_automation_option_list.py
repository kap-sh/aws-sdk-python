"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_multi_select_question_automation_option

EvaluationFormMultiSelectQuestionAutomationOptionList: TypeAlias = list[
    "capo_connect.types.evaluation_form_multi_select_question_automation_option.EvaluationFormMultiSelectQuestionAutomationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: EvaluationFormMultiSelectQuestionAutomationOptionList,
) -> list:
    import capo_connect.types.evaluation_form_multi_select_question_automation_option

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_multi_select_question_automation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> EvaluationFormMultiSelectQuestionAutomationOptionList:
    import capo_connect.types.evaluation_form_multi_select_question_automation_option

    out: EvaluationFormMultiSelectQuestionAutomationOptionList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_multi_select_question_automation_option.deserialize_json(
                item
            )
        )
    return out

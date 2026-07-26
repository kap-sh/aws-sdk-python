"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_single_select_question_automation_option

EvaluationFormSingleSelectQuestionAutomationOptionList: TypeAlias = list[
    "capo_connect.types.evaluation_form_single_select_question_automation_option.EvaluationFormSingleSelectQuestionAutomationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: EvaluationFormSingleSelectQuestionAutomationOptionList,
) -> list:
    import capo_connect.types.evaluation_form_single_select_question_automation_option

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_single_select_question_automation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> EvaluationFormSingleSelectQuestionAutomationOptionList:
    import capo_connect.types.evaluation_form_single_select_question_automation_option

    out: EvaluationFormSingleSelectQuestionAutomationOptionList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_single_select_question_automation_option.deserialize_json(
                item
            )
        )
    return out

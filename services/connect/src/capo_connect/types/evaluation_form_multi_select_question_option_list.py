"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_multi_select_question_option

EvaluationFormMultiSelectQuestionOptionList: TypeAlias = list[
    "capo_connect.types.evaluation_form_multi_select_question_option.EvaluationFormMultiSelectQuestionOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionOptionList) -> list:
    import capo_connect.types.evaluation_form_multi_select_question_option

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_multi_select_question_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormMultiSelectQuestionOptionList:
    import capo_connect.types.evaluation_form_multi_select_question_option

    out: EvaluationFormMultiSelectQuestionOptionList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_multi_select_question_option.deserialize_json(
                item
            )
        )
    return out

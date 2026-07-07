"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source
    import aws_sdk_connect.types.reference_id_list


class EvaluationFormMultiSelectQuestionAutomation(TypedDict, closed=True):
    options: NotRequired[
        "aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list.EvaluationFormMultiSelectQuestionAutomationOptionList"
    ]
    """<p>Automation options for the multi-select question.</p>"""
    default_option_ref_ids: NotRequired[
        "aws_sdk_connect.types.reference_id_list.ReferenceIdList"
    ]
    """<p>Reference IDs of default options.</p>"""
    answer_source: NotRequired[
        "aws_sdk_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionAutomation) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list

        out["Options"] = (
            aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list.serialize_json(
                value["options"]
            )
        )
    if "default_option_ref_ids" in value:
        import aws_sdk_connect.types.reference_id_list

        out["DefaultOptionRefIds"] = (
            aws_sdk_connect.types.reference_id_list.serialize_json(
                value["default_option_ref_ids"]
            )
        )
    if "answer_source" in value:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["AnswerSource"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["answer_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionAutomation:
    out: EvaluationFormMultiSelectQuestionAutomation = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list

        out["options"] = (
            aws_sdk_connect.types.evaluation_form_multi_select_question_automation_option_list.deserialize_json(
                data["Options"]
            )
        )
    if "DefaultOptionRefIds" in data:
        import aws_sdk_connect.types.reference_id_list

        out["default_option_ref_ids"] = (
            aws_sdk_connect.types.reference_id_list.deserialize_json(
                data["DefaultOptionRefIds"]
            )
        )
    if "AnswerSource" in data:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["answer_source"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        )
    return out

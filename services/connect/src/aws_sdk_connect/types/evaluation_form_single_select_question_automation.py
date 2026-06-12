"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source
    import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list
    import aws_sdk_connect.types.reference_id


class EvaluationFormSingleSelectQuestionAutomation(TypedDict):
    options: "aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list.EvaluationFormSingleSelectQuestionAutomationOptionList"
    """<p>The automation options of the single select question.</p>"""
    default_option_ref_id: NotRequired["aws_sdk_connect.types.reference_id.ReferenceId"]
    """<p>The identifier of the default answer option, when none of the automation options match the criteria.</p>"""
    answer_source: NotRequired[
        "aws_sdk_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"
    ]
    """<p>Automation answer source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionAutomation) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list

    out["Options"] = (
        aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list.serialize_json(
            value.get("options", [])
        )
    )
    if "default_option_ref_id" in value:
        out["DefaultOptionRefId"] = value["default_option_ref_id"]
    if "answer_source" in value:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["AnswerSource"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["answer_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionAutomation:
    out: EvaluationFormSingleSelectQuestionAutomation = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list

        out["options"] = (
            aws_sdk_connect.types.evaluation_form_single_select_question_automation_option_list.deserialize_json(
                data["Options"]
            )
        )
    else:
        out["options"] = []
    if "DefaultOptionRefId" in data:
        out["default_option_ref_id"] = data["DefaultOptionRefId"]
    if "AnswerSource" in data:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["answer_source"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        )
    return out

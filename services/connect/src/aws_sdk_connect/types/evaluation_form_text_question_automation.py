"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormTextQuestionAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source


class EvaluationFormTextQuestionAutomation(TypedDict, closed=True):
    answer_source: NotRequired[
        "aws_sdk_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"
    ]
    """<p>Automation answer source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormTextQuestionAutomation) -> dict:
    out: dict = {}
    if "answer_source" in value:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["AnswerSource"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["answer_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormTextQuestionAutomation:
    out: EvaluationFormTextQuestionAutomation = {}  # type: ignore[typeddict-item]
    if "AnswerSource" in data:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        out["answer_source"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        )
    return out

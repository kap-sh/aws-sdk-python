"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionAutomationAnswerSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type


class EvaluationFormQuestionAutomationAnswerSource(TypedDict):
    source_type: "aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type.EvaluationFormQuestionAutomationAnswerSourceType"
    """<p>The automation answer source type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionAutomationAnswerSource) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type

    out["SourceType"] = (
        aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type.serialize_json(
            value["source_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormQuestionAutomationAnswerSource:
    out: EvaluationFormQuestionAutomationAnswerSource = {}  # type: ignore[typeddict-item]
    if "SourceType" in data:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type

        out["source_type"] = (
            aws_sdk_connect.types.evaluation_form_question_automation_answer_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormQuestionAutomationAnswerSource.source_type required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answer_data
    import aws_sdk_connect.types.evaluation_question_answer_analysis_details
    import aws_sdk_connect.types.evaluation_question_answer_analysis_type
    import aws_sdk_connect.types.evaluation_question_input_details
    import aws_sdk_connect.types.evaluation_suggested_answer_status


class EvaluationSuggestedAnswer(TypedDict):
    value: NotRequired[
        "aws_sdk_connect.types.evaluation_answer_data.EvaluationAnswerData"
    ]
    status: "aws_sdk_connect.types.evaluation_suggested_answer_status.EvaluationSuggestedAnswerStatus"
    """<p>The status of the suggested answer. D</p>"""
    input: NotRequired[
        "aws_sdk_connect.types.evaluation_question_input_details.EvaluationQuestionInputDetails"
    ]
    """<p>Details about the input used to question automation.</p>"""
    analysis_type: "aws_sdk_connect.types.evaluation_question_answer_analysis_type.EvaluationQuestionAnswerAnalysisType"
    """<p>Type of analysis used to provide suggested answer.</p>"""
    analysis_details: NotRequired[
        "aws_sdk_connect.types.evaluation_question_answer_analysis_details.EvaluationQuestionAnswerAnalysisDetails"
    ]
    """<p>Detailed analysis results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSuggestedAnswer) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_connect.types.evaluation_answer_data

        out["Value"] = aws_sdk_connect.types.evaluation_answer_data.serialize_json(
            value["value"]
        )
    import aws_sdk_connect.types.evaluation_suggested_answer_status

    out["Status"] = (
        aws_sdk_connect.types.evaluation_suggested_answer_status.serialize_json(
            value["status"]
        )
    )
    if "input" in value:
        import aws_sdk_connect.types.evaluation_question_input_details

        out["Input"] = (
            aws_sdk_connect.types.evaluation_question_input_details.serialize_json(
                value["input"]
            )
        )
    import aws_sdk_connect.types.evaluation_question_answer_analysis_type

    out["AnalysisType"] = (
        aws_sdk_connect.types.evaluation_question_answer_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "analysis_details" in value:
        import aws_sdk_connect.types.evaluation_question_answer_analysis_details

        out["AnalysisDetails"] = (
            aws_sdk_connect.types.evaluation_question_answer_analysis_details.serialize_json(
                value["analysis_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSuggestedAnswer:
    out: EvaluationSuggestedAnswer = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import aws_sdk_connect.types.evaluation_answer_data

        out["value"] = aws_sdk_connect.types.evaluation_answer_data.deserialize_json(
            data["Value"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.evaluation_suggested_answer_status

        out["status"] = (
            aws_sdk_connect.types.evaluation_suggested_answer_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationSuggestedAnswer.status required")
    if "Input" in data:
        import aws_sdk_connect.types.evaluation_question_input_details

        out["input"] = (
            aws_sdk_connect.types.evaluation_question_input_details.deserialize_json(
                data["Input"]
            )
        )
    if "AnalysisType" in data:
        import aws_sdk_connect.types.evaluation_question_answer_analysis_type

        out["analysis_type"] = (
            aws_sdk_connect.types.evaluation_question_answer_analysis_type.deserialize_json(
                data["AnalysisType"]
            )
        )
    else:
        raise DeserializationError("EvaluationSuggestedAnswer.analysis_type required")
    if "AnalysisDetails" in data:
        import aws_sdk_connect.types.evaluation_question_answer_analysis_details

        out["analysis_details"] = (
            aws_sdk_connect.types.evaluation_question_answer_analysis_details.deserialize_json(
                data["AnalysisDetails"]
            )
        )
    return out

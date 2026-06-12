"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answer_data
    import aws_sdk_connect.types.evaluation_suggested_answers_list


class EvaluationAnswerOutput(TypedDict):
    value: NotRequired[
        "aws_sdk_connect.types.evaluation_answer_data.EvaluationAnswerData"
    ]
    """<p>The value for an answer in a contact evaluation.</p>"""
    system_suggested_value: NotRequired[
        "aws_sdk_connect.types.evaluation_answer_data.EvaluationAnswerData"
    ]
    """<p>The system suggested value for an answer in a contact evaluation.</p>"""
    suggested_answers: NotRequired[
        "aws_sdk_connect.types.evaluation_suggested_answers_list.EvaluationSuggestedAnswersList"
    ]
    """<p>Automation suggested answers for the questions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerOutput) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_connect.types.evaluation_answer_data

        out["Value"] = aws_sdk_connect.types.evaluation_answer_data.serialize_json(
            value["value"]
        )
    if "system_suggested_value" in value:
        import aws_sdk_connect.types.evaluation_answer_data

        out["SystemSuggestedValue"] = (
            aws_sdk_connect.types.evaluation_answer_data.serialize_json(
                value["system_suggested_value"]
            )
        )
    if "suggested_answers" in value:
        import aws_sdk_connect.types.evaluation_suggested_answers_list

        out["SuggestedAnswers"] = (
            aws_sdk_connect.types.evaluation_suggested_answers_list.serialize_json(
                value["suggested_answers"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationAnswerOutput:
    out: EvaluationAnswerOutput = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import aws_sdk_connect.types.evaluation_answer_data

        out["value"] = aws_sdk_connect.types.evaluation_answer_data.deserialize_json(
            data["Value"]
        )
    if "SystemSuggestedValue" in data:
        import aws_sdk_connect.types.evaluation_answer_data

        out["system_suggested_value"] = (
            aws_sdk_connect.types.evaluation_answer_data.deserialize_json(
                data["SystemSuggestedValue"]
            )
        )
    if "SuggestedAnswers" in data:
        import aws_sdk_connect.types.evaluation_suggested_answers_list

        out["suggested_answers"] = (
            aws_sdk_connect.types.evaluation_suggested_answers_list.deserialize_json(
                data["SuggestedAnswers"]
            )
        )
    return out

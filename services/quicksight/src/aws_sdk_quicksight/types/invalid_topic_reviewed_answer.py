"""Generated from Smithy shape ``com.amazonaws.quicksight#InvalidTopicReviewedAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.answer_id
    import aws_sdk_quicksight.types.reviewed_answer_error_code


class InvalidTopicReviewedAnswer(TypedDict):
    answer_id: NotRequired["aws_sdk_quicksight.types.answer_id.AnswerId"]
    """<p>The answer ID for the <code>InvalidTopicReviewedAnswer</code>.</p>"""
    error: NotRequired[
        "aws_sdk_quicksight.types.reviewed_answer_error_code.ReviewedAnswerErrorCode"
    ]
    """<p>The error that is returned for the <code>InvalidTopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTopicReviewedAnswer) -> dict:
    out: dict = {}
    if "answer_id" in value:
        out["AnswerId"] = value["answer_id"]
    if "error" in value:
        import aws_sdk_quicksight.types.reviewed_answer_error_code

        out["Error"] = (
            aws_sdk_quicksight.types.reviewed_answer_error_code.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvalidTopicReviewedAnswer:
    out: InvalidTopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    if "Error" in data:
        import aws_sdk_quicksight.types.reviewed_answer_error_code

        out["error"] = (
            aws_sdk_quicksight.types.reviewed_answer_error_code.deserialize_json(
                data["Error"]
            )
        )
    return out

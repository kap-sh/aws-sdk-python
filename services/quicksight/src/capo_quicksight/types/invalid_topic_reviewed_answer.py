"""Generated from Smithy shape ``com.amazonaws.quicksight#InvalidTopicReviewedAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.answer_id
    import capo_quicksight.types.reviewed_answer_error_code


class InvalidTopicReviewedAnswer(TypedDict, closed=True):
    answer_id: NotRequired["capo_quicksight.types.answer_id.AnswerId"]
    """<p>The answer ID for the <code>InvalidTopicReviewedAnswer</code>.</p>"""
    error: NotRequired[
        "capo_quicksight.types.reviewed_answer_error_code.ReviewedAnswerErrorCode"
    ]
    """<p>The error that is returned for the <code>InvalidTopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTopicReviewedAnswer) -> dict:
    out: dict = {}
    if "answer_id" in value:
        out["AnswerId"] = value["answer_id"]
    if "error" in value:
        import capo_quicksight.types.reviewed_answer_error_code

        out["Error"] = capo_quicksight.types.reviewed_answer_error_code.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> InvalidTopicReviewedAnswer:
    out: InvalidTopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    if "Error" in data:
        import capo_quicksight.types.reviewed_answer_error_code

        out["error"] = (
            capo_quicksight.types.reviewed_answer_error_code.deserialize_json(
                data["Error"]
            )
        )
    return out

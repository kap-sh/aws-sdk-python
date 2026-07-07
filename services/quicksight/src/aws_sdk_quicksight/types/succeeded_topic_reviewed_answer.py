"""Generated from Smithy shape ``com.amazonaws.quicksight#SucceededTopicReviewedAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.answer_id


class SucceededTopicReviewedAnswer(TypedDict, closed=True):
    answer_id: NotRequired["aws_sdk_quicksight.types.answer_id.AnswerId"]
    """<p>The answer ID for the <code>SucceededTopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SucceededTopicReviewedAnswer) -> dict:
    out: dict = {}
    if "answer_id" in value:
        out["AnswerId"] = value["answer_id"]
    return out


def deserialize_json(data: dict) -> SucceededTopicReviewedAnswer:
    out: SucceededTopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    return out

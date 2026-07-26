"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteTopicReviewedAnswerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.answer_ids
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.topic_id


class BatchDeleteTopicReviewedAnswerRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that you want to delete a reviewed answers in.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID for the topic reviewed answer that you want to delete. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    answer_ids: NotRequired["capo_quicksight.types.answer_ids.AnswerIds"]
    """<p>The Answer IDs of the Answers to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTopicReviewedAnswerRequest) -> dict:
    out: dict = {}
    if "answer_ids" in value:
        import capo_quicksight.types.answer_ids

        out["AnswerIds"] = capo_quicksight.types.answer_ids.serialize_json(
            value["answer_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteTopicReviewedAnswerRequest:
    out: BatchDeleteTopicReviewedAnswerRequest = {}  # type: ignore[typeddict-item]
    if "AnswerIds" in data:
        import capo_quicksight.types.answer_ids

        out["answer_ids"] = capo_quicksight.types.answer_ids.deserialize_json(
            data["AnswerIds"]
        )
    return out

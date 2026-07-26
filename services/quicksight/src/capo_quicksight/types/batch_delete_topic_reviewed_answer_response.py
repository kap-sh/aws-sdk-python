"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteTopicReviewedAnswerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.invalid_topic_reviewed_answers
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.succeeded_topic_reviewed_answers
    import capo_quicksight.types.topic_id


class BatchDeleteTopicReviewedAnswerResponse(TypedDict, closed=True):
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic reviewed answer that you want to delete. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    succeeded_answers: NotRequired[
        "capo_quicksight.types.succeeded_topic_reviewed_answers.SucceededTopicReviewedAnswers"
    ]
    """<p>The definition of Answers that are successfully deleted.</p>"""
    invalid_answers: NotRequired[
        "capo_quicksight.types.invalid_topic_reviewed_answers.InvalidTopicReviewedAnswers"
    ]
    """<p>The definition of Answers that are invalid and not deleted.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTopicReviewedAnswerResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "succeeded_answers" in value:
        import capo_quicksight.types.succeeded_topic_reviewed_answers

        out["SucceededAnswers"] = (
            capo_quicksight.types.succeeded_topic_reviewed_answers.serialize_json(
                value["succeeded_answers"]
            )
        )
    if "invalid_answers" in value:
        import capo_quicksight.types.invalid_topic_reviewed_answers

        out["InvalidAnswers"] = (
            capo_quicksight.types.invalid_topic_reviewed_answers.serialize_json(
                value["invalid_answers"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteTopicReviewedAnswerResponse:
    out: BatchDeleteTopicReviewedAnswerResponse = {}  # type: ignore[typeddict-item]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "SucceededAnswers" in data:
        import capo_quicksight.types.succeeded_topic_reviewed_answers

        out["succeeded_answers"] = (
            capo_quicksight.types.succeeded_topic_reviewed_answers.deserialize_json(
                data["SucceededAnswers"]
            )
        )
    if "InvalidAnswers" in data:
        import capo_quicksight.types.invalid_topic_reviewed_answers

        out["invalid_answers"] = (
            capo_quicksight.types.invalid_topic_reviewed_answers.deserialize_json(
                data["InvalidAnswers"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

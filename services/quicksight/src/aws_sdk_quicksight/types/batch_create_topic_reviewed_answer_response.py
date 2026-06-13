"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchCreateTopicReviewedAnswerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.invalid_topic_reviewed_answers
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.succeeded_topic_reviewed_answers
    import aws_sdk_quicksight.types.topic_id


class BatchCreateTopicReviewedAnswerResponse(TypedDict):
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID for the topic reviewed answer that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    succeeded_answers: NotRequired[
        "aws_sdk_quicksight.types.succeeded_topic_reviewed_answers.SucceededTopicReviewedAnswers"
    ]
    """<p>The definition of Answers that are successfully created.</p>"""
    invalid_answers: NotRequired[
        "aws_sdk_quicksight.types.invalid_topic_reviewed_answers.InvalidTopicReviewedAnswers"
    ]
    """<p>The definition of Answers that are invalid and not created.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateTopicReviewedAnswerResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "succeeded_answers" in value:
        import aws_sdk_quicksight.types.succeeded_topic_reviewed_answers

        out["SucceededAnswers"] = (
            aws_sdk_quicksight.types.succeeded_topic_reviewed_answers.serialize_json(
                value["succeeded_answers"]
            )
        )
    if "invalid_answers" in value:
        import aws_sdk_quicksight.types.invalid_topic_reviewed_answers

        out["InvalidAnswers"] = (
            aws_sdk_quicksight.types.invalid_topic_reviewed_answers.serialize_json(
                value["invalid_answers"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> BatchCreateTopicReviewedAnswerResponse:
    out: BatchCreateTopicReviewedAnswerResponse = {}  # type: ignore[typeddict-item]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "SucceededAnswers" in data:
        import aws_sdk_quicksight.types.succeeded_topic_reviewed_answers

        out["succeeded_answers"] = (
            aws_sdk_quicksight.types.succeeded_topic_reviewed_answers.deserialize_json(
                data["SucceededAnswers"]
            )
        )
    if "InvalidAnswers" in data:
        import aws_sdk_quicksight.types.invalid_topic_reviewed_answers

        out["invalid_answers"] = (
            aws_sdk_quicksight.types.invalid_topic_reviewed_answers.deserialize_json(
                data["InvalidAnswers"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

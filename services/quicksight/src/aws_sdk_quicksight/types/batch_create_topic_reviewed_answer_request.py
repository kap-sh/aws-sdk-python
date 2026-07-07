"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchCreateTopicReviewedAnswerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.create_topic_reviewed_answers
    import aws_sdk_quicksight.types.topic_id


class BatchCreateTopicReviewedAnswerRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that you want to create a reviewed answer in.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID for the topic reviewed answer that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    answers: "aws_sdk_quicksight.types.create_topic_reviewed_answers.CreateTopicReviewedAnswers"
    """<p>The definition of the Answers to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateTopicReviewedAnswerRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.create_topic_reviewed_answers

    out["Answers"] = (
        aws_sdk_quicksight.types.create_topic_reviewed_answers.serialize_json(
            value["answers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateTopicReviewedAnswerRequest:
    out: BatchCreateTopicReviewedAnswerRequest = {}  # type: ignore[typeddict-item]
    if "Answers" in data:
        import aws_sdk_quicksight.types.create_topic_reviewed_answers

        out["answers"] = (
            aws_sdk_quicksight.types.create_topic_reviewed_answers.deserialize_json(
                data["Answers"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateTopicReviewedAnswerRequest.answers required"
        )
    return out

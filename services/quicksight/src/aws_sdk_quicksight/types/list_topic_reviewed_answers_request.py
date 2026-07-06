"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicReviewedAnswersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.topic_id


class ListTopicReviewedAnswersRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that containd the reviewed answers that you want listed.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID for the topic that contains the reviewed answer that you want to list. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicReviewedAnswersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicReviewedAnswersRequest:
    out: ListTopicReviewedAnswersRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.topic_id


class DescribeTopicRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTopicRequest:
    out: DescribeTopicRequest = {}  # type: ignore[typeddict-item]
    return out

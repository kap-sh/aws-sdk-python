"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.topic_id


class DescribeTopicPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want described.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTopicPermissionsRequest:
    out: DescribeTopicPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRefreshRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.topic_id


class DescribeTopicRefreshRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic whose refresh you want to describe.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    refresh_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the refresh, which is performed when the topic is created or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRefreshRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTopicRefreshRequest:
    out: DescribeTopicRefreshRequest = {}  # type: ignore[typeddict-item]
    return out

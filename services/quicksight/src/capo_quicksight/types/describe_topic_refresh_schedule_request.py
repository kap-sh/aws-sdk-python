"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRefreshScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id


class DescribeTopicRefreshScheduleRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that contains the refresh schedule that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    dataset_id: "capo_quicksight.types.string.String"
    """<p>The ID of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRefreshScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTopicRefreshScheduleRequest:
    out: DescribeTopicRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    return out

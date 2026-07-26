"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicRefreshSchedulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.topic_id


class ListTopicRefreshSchedulesRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic whose refresh schedule you want described.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID for the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRefreshSchedulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTopicRefreshSchedulesRequest:
    out: ListTopicRefreshSchedulesRequest = {}  # type: ignore[typeddict-item]
    return out

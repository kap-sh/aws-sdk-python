"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueueLimitAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.queue_id


class ListQueueLimitAssociationsRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the limits and associations.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of associations to return in each page of results.</p>"""
    queue_id: NotRequired["aws_sdk_deadline.types.queue_id.QueueId"]
    """<p>Specifies that the operation should return only the queue limit associations for the specified queue. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>"""
    limit_id: NotRequired["aws_sdk_deadline.types.limit_id.LimitId"]
    """<p>Specifies that the operation should return only the queue limit associations for the specified limit. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueueLimitAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueueLimitAssociationsRequest:
    out: ListQueueLimitAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out

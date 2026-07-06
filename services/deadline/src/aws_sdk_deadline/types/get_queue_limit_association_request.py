"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.queue_id


class GetQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the associated queue and limit.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue associated with the limit.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit associated with the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueLimitAssociationRequest:
    out: GetQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    return out

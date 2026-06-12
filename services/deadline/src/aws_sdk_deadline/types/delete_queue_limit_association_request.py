"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.queue_id


class DeleteQueueLimitAssociationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the queue and limit to disassociate.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue to disassociate.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueLimitAssociationRequest:
    out: DeleteQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    return out

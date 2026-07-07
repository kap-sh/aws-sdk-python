"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.queue_id


class CreateQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the queue and limit to associate.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue to associate with the limit.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to associate with the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["limitId"] = value["limit_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueLimitAssociationRequest:
    out: CreateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError(
            "CreateQueueLimitAssociationRequest.queue_id required"
        )
    if "limitId" in data:
        out["limit_id"] = data["limitId"]
    else:
        raise DeserializationError(
            "CreateQueueLimitAssociationRequest.limit_id required"
        )
    return out

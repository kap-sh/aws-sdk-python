"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.update_queue_limit_association_status


class UpdateQueueLimitAssociationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the associated queues and limits.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue associated to the limit.</p>"""
    limit_id: "aws_sdk_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit associated to the queue.</p>"""
    status: "aws_sdk_deadline.types.update_queue_limit_association_status.UpdateQueueLimitAssociationStatus"
    """<p>Sets the status of the limit. You can mark the limit active, or you can stop usage of the limit and either complete existing tasks or cancel any existing tasks immediately. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.update_queue_limit_association_status

    out["status"] = (
        aws_sdk_deadline.types.update_queue_limit_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueLimitAssociationRequest:
    out: UpdateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_deadline.types.update_queue_limit_association_status

        out["status"] = (
            aws_sdk_deadline.types.update_queue_limit_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateQueueLimitAssociationRequest.status required")
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.queue_id


class DeleteQueueFleetAssociationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that holds the queue-fleet association.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue-fleet association.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the queue-fleet association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueFleetAssociationRequest:
    out: DeleteQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    return out

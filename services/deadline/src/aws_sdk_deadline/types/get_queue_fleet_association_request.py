"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.queue_id


class GetQueueFleetAssociationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the queue-fleet association.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue-fleet association.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID for the queue-fleet association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueFleetAssociationRequest:
    out: GetQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    return out

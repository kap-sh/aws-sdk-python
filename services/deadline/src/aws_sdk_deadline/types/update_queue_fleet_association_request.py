"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.update_queue_fleet_association_status


class UpdateQueueFleetAssociationRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to update.</p>"""
    status: "aws_sdk_deadline.types.update_queue_fleet_association_status.UpdateQueueFleetAssociationStatus"
    """<p>The status to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.update_queue_fleet_association_status

    out["status"] = (
        aws_sdk_deadline.types.update_queue_fleet_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueFleetAssociationRequest:
    out: UpdateQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_deadline.types.update_queue_fleet_association_status

        out["status"] = (
            aws_sdk_deadline.types.update_queue_fleet_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateQueueFleetAssociationRequest.status required")
    return out

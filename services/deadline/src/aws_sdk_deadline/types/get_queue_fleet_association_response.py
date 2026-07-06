"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueFleetAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.queue_fleet_association_status
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetQueueFleetAssociationResponse(TypedDict, closed=True):
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue-fleet association.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID for the queue-fleet association.</p>"""
    status: "aws_sdk_deadline.types.queue_fleet_association_status.QueueFleetAssociationStatus"
    """<p>The status of the queue-fleet association.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueFleetAssociationResponse) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["fleetId"] = value["fleet_id"]
    import aws_sdk_deadline.types.queue_fleet_association_status

    out["status"] = (
        aws_sdk_deadline.types.queue_fleet_association_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> GetQueueFleetAssociationResponse:
    out: GetQueueFleetAssociationResponse = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("GetQueueFleetAssociationResponse.queue_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("GetQueueFleetAssociationResponse.fleet_id required")
    if "status" in data:
        import aws_sdk_deadline.types.queue_fleet_association_status

        out["status"] = (
            aws_sdk_deadline.types.queue_fleet_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetQueueFleetAssociationResponse.status required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "GetQueueFleetAssociationResponse.created_at required"
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError(
            "GetQueueFleetAssociationResponse.created_by required"
        )
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out

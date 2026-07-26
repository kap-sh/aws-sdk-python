"""Generated from Smithy shape ``com.amazonaws.deadline#QueueFleetAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_fleet_association_status
    import capo_deadline.types.queue_id
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class QueueFleetAssociationSummary(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    status: (
        "capo_deadline.types.queue_fleet_association_status.QueueFleetAssociationStatus"
    )
    """<p>The status of task scheduling in the queue-fleet association.</p> <ul> <li> <p> <code>ACTIVE</code>–Association is active.</p> </li> <li> <p> <code>STOP_SCHEDULING_AND_COMPLETE_TASKS</code>–Association has stopped scheduling new tasks and is completing current tasks.</p> </li> <li> <p> <code>STOP_SCHEDULING_AND_CANCEL_TASKS</code>–Association has stopped scheduling new tasks and is canceling current tasks.</p> </li> <li> <p> <code>STOPPED</code>–Association has been stopped.</p> </li> </ul>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueFleetAssociationSummary) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["fleetId"] = value["fleet_id"]
    import capo_deadline.types.queue_fleet_association_status

    out["status"] = capo_deadline.types.queue_fleet_association_status.serialize_json(
        value["status"]
    )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> QueueFleetAssociationSummary:
    out: QueueFleetAssociationSummary = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("QueueFleetAssociationSummary.queue_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("QueueFleetAssociationSummary.fleet_id required")
    if "status" in data:
        import capo_deadline.types.queue_fleet_association_status

        out["status"] = (
            capo_deadline.types.queue_fleet_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("QueueFleetAssociationSummary.status required")
    if "createdAt" in data:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("QueueFleetAssociationSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("QueueFleetAssociationSummary.created_by required")
    if "updatedAt" in data:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out

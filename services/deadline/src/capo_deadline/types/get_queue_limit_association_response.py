"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueLimitAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.queue_limit_association_status
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetQueueLimitAssociationResponse(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue associated with the limit.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit associated with the queue.</p>"""
    status: (
        "capo_deadline.types.queue_limit_association_status.QueueLimitAssociationStatus"
    )
    """<p>The current status of the limit.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The Unix timestamp of the date and time that the association was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user identifier of the person that created the association.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The Unix timestamp of the date and time that the association was last updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user identifier of the person that last updated the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueLimitAssociationResponse) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["limitId"] = value["limit_id"]
    import capo_deadline.types.queue_limit_association_status

    out["status"] = capo_deadline.types.queue_limit_association_status.serialize_json(
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


def deserialize_json(data: dict) -> GetQueueLimitAssociationResponse:
    out: GetQueueLimitAssociationResponse = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("GetQueueLimitAssociationResponse.queue_id required")
    if "limitId" in data:
        out["limit_id"] = data["limitId"]
    else:
        raise DeserializationError("GetQueueLimitAssociationResponse.limit_id required")
    if "status" in data:
        import capo_deadline.types.queue_limit_association_status

        out["status"] = (
            capo_deadline.types.queue_limit_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetQueueLimitAssociationResponse.status required")
    if "createdAt" in data:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "GetQueueLimitAssociationResponse.created_at required"
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError(
            "GetQueueLimitAssociationResponse.created_by required"
        )
    if "updatedAt" in data:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out

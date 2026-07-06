"""Generated from Smithy shape ``com.amazonaws.deadline#QueueSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.default_queue_budget_action
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_blocked_reason
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.queue_status
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class QueueSummary(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the queue summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: "aws_sdk_deadline.types.queue_status.QueueStatus"
    """<p>That status of the queue.</p>"""
    default_budget_action: (
        "aws_sdk_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    )
    """<p>The default action taken on a queue summary if a budget wasn't configured.</p>"""
    blocked_reason: NotRequired[
        "aws_sdk_deadline.types.queue_blocked_reason.QueueBlockedReason"
    ]
    """<p>The reason the queue is blocked, if applicable.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSummary) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["displayName"] = value["display_name"]
    import aws_sdk_deadline.types.queue_status

    out["status"] = aws_sdk_deadline.types.queue_status.serialize_json(value["status"])
    import aws_sdk_deadline.types.default_queue_budget_action

    out["defaultBudgetAction"] = (
        aws_sdk_deadline.types.default_queue_budget_action.serialize_json(
            value["default_budget_action"]
        )
    )
    if "blocked_reason" in value:
        import aws_sdk_deadline.types.queue_blocked_reason

        out["blockedReason"] = (
            aws_sdk_deadline.types.queue_blocked_reason.serialize_json(
                value["blocked_reason"]
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


def deserialize_json(data: dict) -> QueueSummary:
    out: QueueSummary = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("QueueSummary.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("QueueSummary.queue_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("QueueSummary.display_name required")
    if "status" in data:
        import aws_sdk_deadline.types.queue_status

        out["status"] = aws_sdk_deadline.types.queue_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("QueueSummary.status required")
    if "defaultBudgetAction" in data:
        import aws_sdk_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            aws_sdk_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    else:
        raise DeserializationError("QueueSummary.default_budget_action required")
    if "blockedReason" in data:
        import aws_sdk_deadline.types.queue_blocked_reason

        out["blocked_reason"] = (
            aws_sdk_deadline.types.queue_blocked_reason.deserialize_json(
                data["blockedReason"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("QueueSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("QueueSummary.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out

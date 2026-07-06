"""Generated from Smithy shape ``com.amazonaws.deadline#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.session_lifecycle_status
    import aws_sdk_deadline.types.session_lifecycle_target_status
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.worker_id


class SessionSummary(TypedDict, closed=True):
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""
    started_at: "aws_sdk_deadline.types.started_at.StartedAt"
    """<p>The date and time the resource started running.</p>"""
    lifecycle_status: (
        "aws_sdk_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """<p>The life cycle status for the session.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    target_lifecycle_status: NotRequired[
        "aws_sdk_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    ]
    """<p>The target life cycle status for the session.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    import aws_sdk_deadline.types.started_at

    out["startedAt"] = aws_sdk_deadline.types.started_at.serialize_json(
        value["started_at"]
    )
    import aws_sdk_deadline.types.session_lifecycle_status

    out["lifecycleStatus"] = (
        aws_sdk_deadline.types.session_lifecycle_status.serialize_json(
            value["lifecycle_status"]
        )
    )
    if "ended_at" in value:
        import aws_sdk_deadline.types.ended_at

        out["endedAt"] = aws_sdk_deadline.types.ended_at.serialize_json(
            value["ended_at"]
        )
    if "target_lifecycle_status" in value:
        import aws_sdk_deadline.types.session_lifecycle_target_status

        out["targetLifecycleStatus"] = (
            aws_sdk_deadline.types.session_lifecycle_target_status.serialize_json(
                value["target_lifecycle_status"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("SessionSummary.fleet_id required")
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("SessionSummary.worker_id required")
    if "startedAt" in data:
        import aws_sdk_deadline.types.started_at

        out["started_at"] = aws_sdk_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("SessionSummary.started_at required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.session_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.session_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("SessionSummary.lifecycle_status required")
    if "endedAt" in data:
        import aws_sdk_deadline.types.ended_at

        out["ended_at"] = aws_sdk_deadline.types.ended_at.deserialize_json(
            data["endedAt"]
        )
    if "targetLifecycleStatus" in data:
        import aws_sdk_deadline.types.session_lifecycle_target_status

        out["target_lifecycle_status"] = (
            aws_sdk_deadline.types.session_lifecycle_target_status.deserialize_json(
                data["targetLifecycleStatus"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out

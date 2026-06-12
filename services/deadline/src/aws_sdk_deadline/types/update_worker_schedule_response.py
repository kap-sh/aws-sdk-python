"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerScheduleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_sessions
    import aws_sdk_deadline.types.cancel_session_actions
    import aws_sdk_deadline.types.desired_worker_status
    import aws_sdk_deadline.types.update_worker_schedule_interval


class UpdateWorkerScheduleResponse(TypedDict):
    assigned_sessions: "aws_sdk_deadline.types.assigned_sessions.AssignedSessions"
    """<p>The assigned sessions to update.</p>"""
    cancel_session_actions: (
        "aws_sdk_deadline.types.cancel_session_actions.CancelSessionActions"
    )
    """<p>The session actions associated with the worker schedule to cancel.</p>"""
    desired_worker_status: NotRequired[
        "aws_sdk_deadline.types.desired_worker_status.DesiredWorkerStatus"
    ]
    """<p>The status to update the worker to.</p>"""
    update_interval_seconds: "aws_sdk_deadline.types.update_worker_schedule_interval.UpdateWorkerScheduleInterval"
    """<p>Updates the time interval (in seconds) for the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerScheduleResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.assigned_sessions

    out["assignedSessions"] = aws_sdk_deadline.types.assigned_sessions.serialize_json(
        value["assigned_sessions"]
    )
    import aws_sdk_deadline.types.cancel_session_actions

    out["cancelSessionActions"] = (
        aws_sdk_deadline.types.cancel_session_actions.serialize_json(
            value["cancel_session_actions"]
        )
    )
    if "desired_worker_status" in value:
        import aws_sdk_deadline.types.desired_worker_status

        out["desiredWorkerStatus"] = (
            aws_sdk_deadline.types.desired_worker_status.serialize_json(
                value["desired_worker_status"]
            )
        )
    out["updateIntervalSeconds"] = value["update_interval_seconds"]
    return out


def deserialize_json(data: dict) -> UpdateWorkerScheduleResponse:
    out: UpdateWorkerScheduleResponse = {}  # type: ignore[typeddict-item]
    if "assignedSessions" in data:
        import aws_sdk_deadline.types.assigned_sessions

        out["assigned_sessions"] = (
            aws_sdk_deadline.types.assigned_sessions.deserialize_json(
                data["assignedSessions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.assigned_sessions required"
        )
    if "cancelSessionActions" in data:
        import aws_sdk_deadline.types.cancel_session_actions

        out["cancel_session_actions"] = (
            aws_sdk_deadline.types.cancel_session_actions.deserialize_json(
                data["cancelSessionActions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.cancel_session_actions required"
        )
    if "desiredWorkerStatus" in data:
        import aws_sdk_deadline.types.desired_worker_status

        out["desired_worker_status"] = (
            aws_sdk_deadline.types.desired_worker_status.deserialize_json(
                data["desiredWorkerStatus"]
            )
        )
    if "updateIntervalSeconds" in data:
        out["update_interval_seconds"] = data["updateIntervalSeconds"]
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.update_interval_seconds required"
        )
    return out

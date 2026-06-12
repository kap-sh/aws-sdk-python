"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSession``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_session_actions
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.log_configuration
    import aws_sdk_deadline.types.queue_id


class AssignedSession(TypedDict):
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the assigned session.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID for the assigned session.</p>"""
    session_actions: (
        "aws_sdk_deadline.types.assigned_session_actions.AssignedSessionActions"
    )
    """<p>The session actions to apply to the assigned session.</p>"""
    log_configuration: "aws_sdk_deadline.types.log_configuration.LogConfiguration"
    """<p>The log configuration for the worker's assigned session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSession) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    import aws_sdk_deadline.types.assigned_session_actions

    out["sessionActions"] = (
        aws_sdk_deadline.types.assigned_session_actions.serialize_json(
            value["session_actions"]
        )
    )
    import aws_sdk_deadline.types.log_configuration

    out["logConfiguration"] = aws_sdk_deadline.types.log_configuration.serialize_json(
        value["log_configuration"]
    )
    return out


def deserialize_json(data: dict) -> AssignedSession:
    out: AssignedSession = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("AssignedSession.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("AssignedSession.job_id required")
    if "sessionActions" in data:
        import aws_sdk_deadline.types.assigned_session_actions

        out["session_actions"] = (
            aws_sdk_deadline.types.assigned_session_actions.deserialize_json(
                data["sessionActions"]
            )
        )
    else:
        raise DeserializationError("AssignedSession.session_actions required")
    if "logConfiguration" in data:
        import aws_sdk_deadline.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_deadline.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    else:
        raise DeserializationError("AssignedSession.log_configuration required")
    return out

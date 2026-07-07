"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.session_lifecycle_status
    import aws_sdk_deadline.types.session_lifecycle_target_status
    import aws_sdk_deadline.types.started_at


class WorkerSessionSummary(TypedDict, closed=True):
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID for the session action.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue associated to the worker.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID for the job associated with the worker's session.</p>"""
    started_at: "aws_sdk_deadline.types.started_at.StartedAt"
    """<p>The date and time the resource started running.</p>"""
    lifecycle_status: (
        "aws_sdk_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """<p>The life cycle status for the worker's session.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    target_lifecycle_status: NotRequired[
        "aws_sdk_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    ]
    """<p>The life cycle status </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
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
    return out


def deserialize_json(data: dict) -> WorkerSessionSummary:
    out: WorkerSessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("WorkerSessionSummary.session_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("WorkerSessionSummary.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("WorkerSessionSummary.job_id required")
    if "startedAt" in data:
        import aws_sdk_deadline.types.started_at

        out["started_at"] = aws_sdk_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("WorkerSessionSummary.started_at required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.session_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.session_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("WorkerSessionSummary.lifecycle_status required")
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
    return out

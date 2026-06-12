"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.host_properties_response
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.log_configuration
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.session_lifecycle_status
    import aws_sdk_deadline.types.session_lifecycle_target_status
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.worker_id


class BatchGetSessionItem(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the session.</p>"""
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the session.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID of the session.</p>"""
    started_at: "aws_sdk_deadline.types.started_at.StartedAt"
    """<p>The date and time the resource started running.</p>"""
    lifecycle_status: (
        "aws_sdk_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """<p>The life cycle status of the session.</p>"""
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
    log: "aws_sdk_deadline.types.log_configuration.LogConfiguration"
    """<p>The session log.</p>"""
    host_properties: NotRequired[
        "aws_sdk_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """<p>The host properties for the session.</p>"""
    worker_log: NotRequired["aws_sdk_deadline.types.log_configuration.LogConfiguration"]
    """<p>The worker log for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
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
    import aws_sdk_deadline.types.log_configuration

    out["log"] = aws_sdk_deadline.types.log_configuration.serialize_json(value["log"])
    if "host_properties" in value:
        import aws_sdk_deadline.types.host_properties_response

        out["hostProperties"] = (
            aws_sdk_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    if "worker_log" in value:
        import aws_sdk_deadline.types.log_configuration

        out["workerLog"] = aws_sdk_deadline.types.log_configuration.serialize_json(
            value["worker_log"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetSessionItem:
    out: BatchGetSessionItem = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetSessionItem.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetSessionItem.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetSessionItem.job_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("BatchGetSessionItem.session_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("BatchGetSessionItem.fleet_id required")
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("BatchGetSessionItem.worker_id required")
    if "startedAt" in data:
        import aws_sdk_deadline.types.started_at

        out["started_at"] = aws_sdk_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("BatchGetSessionItem.started_at required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.session_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.session_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionItem.lifecycle_status required")
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
    if "log" in data:
        import aws_sdk_deadline.types.log_configuration

        out["log"] = aws_sdk_deadline.types.log_configuration.deserialize_json(
            data["log"]
        )
    else:
        raise DeserializationError("BatchGetSessionItem.log required")
    if "hostProperties" in data:
        import aws_sdk_deadline.types.host_properties_response

        out["host_properties"] = (
            aws_sdk_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if "workerLog" in data:
        import aws_sdk_deadline.types.log_configuration

        out["worker_log"] = aws_sdk_deadline.types.log_configuration.deserialize_json(
            data["workerLog"]
        )
    return out

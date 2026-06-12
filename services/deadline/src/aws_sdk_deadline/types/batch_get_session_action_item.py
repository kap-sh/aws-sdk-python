"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.acquired_limits
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.process_exit_code
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_action_definition
    import aws_sdk_deadline.types.session_action_id
    import aws_sdk_deadline.types.session_action_progress_message
    import aws_sdk_deadline.types.session_action_progress_percent
    import aws_sdk_deadline.types.session_action_status
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.task_run_manifest_properties_list_response
    import aws_sdk_deadline.types.timestamp


class BatchGetSessionActionItem(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session action.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session action.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the session action.</p>"""
    session_action_id: "aws_sdk_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID.</p>"""
    status: "aws_sdk_deadline.types.session_action_status.SessionActionStatus"
    """<p>The status of the session action.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    worker_updated_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the resource was updated by a worker.</p>"""
    progress_percent: NotRequired[
        "aws_sdk_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """<p>The completion percentage for the session action.</p>"""
    manifests: NotRequired[
        "aws_sdk_deadline.types.task_run_manifest_properties_list_response.TaskRunManifestPropertiesListResponse"
    ]
    """<p>The manifests for the session action.</p>"""
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID for the session action.</p>"""
    process_exit_code: NotRequired[
        "aws_sdk_deadline.types.process_exit_code.ProcessExitCode"
    ]
    """<p>The exit code to apply to the session action.</p>"""
    progress_message: NotRequired[
        "aws_sdk_deadline.types.session_action_progress_message.SessionActionProgressMessage"
    ]
    """<p>The message that communicates the progress of the session action.</p>"""
    acquired_limits: NotRequired[
        "aws_sdk_deadline.types.acquired_limits.AcquiredLimits"
    ]
    """<p>The limits that were acquired for the session action.</p>"""
    definition: (
        "aws_sdk_deadline.types.session_action_definition.SessionActionDefinition"
    )
    """<p>The session action definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionActionId"] = value["session_action_id"]
    import aws_sdk_deadline.types.session_action_status

    out["status"] = aws_sdk_deadline.types.session_action_status.serialize_json(
        value["status"]
    )
    if "started_at" in value:
        import aws_sdk_deadline.types.started_at

        out["startedAt"] = aws_sdk_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_deadline.types.ended_at

        out["endedAt"] = aws_sdk_deadline.types.ended_at.serialize_json(
            value["ended_at"]
        )
    if "worker_updated_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["workerUpdatedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["worker_updated_at"]
        )
    if "progress_percent" in value:
        out["progressPercent"] = value["progress_percent"]
    if "manifests" in value:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_response.serialize_json(
                value["manifests"]
            )
        )
    out["sessionId"] = value["session_id"]
    if "process_exit_code" in value:
        out["processExitCode"] = value["process_exit_code"]
    if "progress_message" in value:
        out["progressMessage"] = value["progress_message"]
    if "acquired_limits" in value:
        import aws_sdk_deadline.types.acquired_limits

        out["acquiredLimits"] = aws_sdk_deadline.types.acquired_limits.serialize_json(
            value["acquired_limits"]
        )
    import aws_sdk_deadline.types.session_action_definition

    out["definition"] = aws_sdk_deadline.types.session_action_definition.serialize_json(
        value["definition"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionItem:
    out: BatchGetSessionActionItem = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetSessionActionItem.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetSessionActionItem.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetSessionActionItem.job_id required")
    if "sessionActionId" in data:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError(
            "BatchGetSessionActionItem.session_action_id required"
        )
    if "status" in data:
        import aws_sdk_deadline.types.session_action_status

        out["status"] = aws_sdk_deadline.types.session_action_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("BatchGetSessionActionItem.status required")
    if "startedAt" in data:
        import aws_sdk_deadline.types.started_at

        out["started_at"] = aws_sdk_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_deadline.types.ended_at

        out["ended_at"] = aws_sdk_deadline.types.ended_at.deserialize_json(
            data["endedAt"]
        )
    if "workerUpdatedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["worker_updated_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["workerUpdatedAt"]
        )
    if "progressPercent" in data:
        out["progress_percent"] = data["progressPercent"]
    if "manifests" in data:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_response.deserialize_json(
                data["manifests"]
            )
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("BatchGetSessionActionItem.session_id required")
    if "processExitCode" in data:
        out["process_exit_code"] = data["processExitCode"]
    if "progressMessage" in data:
        out["progress_message"] = data["progressMessage"]
    if "acquiredLimits" in data:
        import aws_sdk_deadline.types.acquired_limits

        out["acquired_limits"] = (
            aws_sdk_deadline.types.acquired_limits.deserialize_json(
                data["acquiredLimits"]
            )
        )
    if "definition" in data:
        import aws_sdk_deadline.types.session_action_definition

        out["definition"] = (
            aws_sdk_deadline.types.session_action_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionActionItem.definition required")
    return out

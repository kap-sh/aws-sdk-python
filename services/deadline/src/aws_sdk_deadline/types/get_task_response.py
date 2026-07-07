"""Generated from Smithy shape ``com.amazonaws.deadline#GetTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.session_action_id
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.task_id
    import aws_sdk_deadline.types.task_parameters
    import aws_sdk_deadline.types.task_retry_count
    import aws_sdk_deadline.types.task_run_status
    import aws_sdk_deadline.types.task_target_run_status
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetTaskResponse(TypedDict, closed=True):
    task_id: "aws_sdk_deadline.types.task_id.TaskId"
    """<p>The task ID.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    run_status: "aws_sdk_deadline.types.task_run_status.TaskRunStatus"
    """<p>The run status for the task.</p>"""
    target_run_status: NotRequired[
        "aws_sdk_deadline.types.task_target_run_status.TaskTargetRunStatus"
    ]
    """<p>The run status with which to start the task.</p>"""
    failure_retry_count: NotRequired[
        "aws_sdk_deadline.types.task_retry_count.TaskRetryCount"
    ]
    """<p>The number of times that the task failed and was retried.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    latest_session_action_id: NotRequired[
        "aws_sdk_deadline.types.session_action_id.SessionActionId"
    ]
    """<p>The latest session action ID for the task.</p>"""
    parameters: NotRequired["aws_sdk_deadline.types.task_parameters.TaskParameters"]
    """<p>The parameters for the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    import aws_sdk_deadline.types.task_run_status

    out["runStatus"] = aws_sdk_deadline.types.task_run_status.serialize_json(
        value["run_status"]
    )
    if "target_run_status" in value:
        import aws_sdk_deadline.types.task_target_run_status

        out["targetRunStatus"] = (
            aws_sdk_deadline.types.task_target_run_status.serialize_json(
                value["target_run_status"]
            )
        )
    if "failure_retry_count" in value:
        out["failureRetryCount"] = value["failure_retry_count"]
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
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "latest_session_action_id" in value:
        out["latestSessionActionId"] = value["latest_session_action_id"]
    if "parameters" in value:
        import aws_sdk_deadline.types.task_parameters

        out["parameters"] = aws_sdk_deadline.types.task_parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> GetTaskResponse:
    out: GetTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("GetTaskResponse.task_id required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetTaskResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetTaskResponse.created_by required")
    if "runStatus" in data:
        import aws_sdk_deadline.types.task_run_status

        out["run_status"] = aws_sdk_deadline.types.task_run_status.deserialize_json(
            data["runStatus"]
        )
    else:
        raise DeserializationError("GetTaskResponse.run_status required")
    if "targetRunStatus" in data:
        import aws_sdk_deadline.types.task_target_run_status

        out["target_run_status"] = (
            aws_sdk_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    if "failureRetryCount" in data:
        out["failure_retry_count"] = data["failureRetryCount"]
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
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "latestSessionActionId" in data:
        out["latest_session_action_id"] = data["latestSessionActionId"]
    if "parameters" in data:
        import aws_sdk_deadline.types.task_parameters

        out["parameters"] = aws_sdk_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
        )
    return out

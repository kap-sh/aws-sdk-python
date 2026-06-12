"""Generated from Smithy shape ``com.amazonaws.deadline#StepSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.dependency_counts
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.step_lifecycle_status
    import aws_sdk_deadline.types.step_name
    import aws_sdk_deadline.types.step_target_task_run_status
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.task_failure_retry_count
    import aws_sdk_deadline.types.task_run_status
    import aws_sdk_deadline.types.task_run_status_counts
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class StepSummary(TypedDict):
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    name: "aws_sdk_deadline.types.step_name.StepName"
    """<p>The name of the step.</p>"""
    lifecycle_status: "aws_sdk_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    """<p>The life cycle status.</p>"""
    lifecycle_status_message: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>A message that describes the lifecycle of the step.</p>"""
    task_run_status: "aws_sdk_deadline.types.task_run_status.TaskRunStatus"
    """<p>The task run status for the job.</p> <ul> <li> <p> <code>PENDING</code>–pending and waiting for resources.</p> </li> <li> <p> <code>READY</code>–ready to process.</p> </li> <li> <p> <code>ASSIGNED</code>–assigned and will run next on a worker.</p> </li> <li> <p> <code>SCHEDULED</code>–scheduled to run on a worker.</p> </li> <li> <p> <code>INTERRUPTING</code>–being interrupted.</p> </li> <li> <p> <code>RUNNING</code>–running on a worker.</p> </li> <li> <p> <code>SUSPENDED</code>–the task is suspended.</p> </li> <li> <p> <code>CANCELED</code>–the task has been canceled.</p> </li> <li> <p> <code>FAILED</code>–the task has failed.</p> </li> <li> <p> <code>SUCCEEDED</code>–the task has succeeded.</p> </li> </ul>"""
    task_run_status_counts: (
        "aws_sdk_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    )
    """<p>The number of tasks running on the job.</p>"""
    task_failure_retry_count: NotRequired[
        "aws_sdk_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The total number of times tasks from the step failed and were retried.</p>"""
    target_task_run_status: NotRequired[
        "aws_sdk_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """<p>The task status to update the job's tasks to.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    dependency_counts: NotRequired[
        "aws_sdk_deadline.types.dependency_counts.DependencyCounts"
    ]
    """<p>The number of dependencies for the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepSummary) -> dict:
    out: dict = {}
    out["stepId"] = value["step_id"]
    out["name"] = value["name"]
    import aws_sdk_deadline.types.step_lifecycle_status

    out["lifecycleStatus"] = (
        aws_sdk_deadline.types.step_lifecycle_status.serialize_json(
            value["lifecycle_status"]
        )
    )
    if "lifecycle_status_message" in value:
        out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    import aws_sdk_deadline.types.task_run_status

    out["taskRunStatus"] = aws_sdk_deadline.types.task_run_status.serialize_json(
        value["task_run_status"]
    )
    import aws_sdk_deadline.types.task_run_status_counts

    out["taskRunStatusCounts"] = (
        aws_sdk_deadline.types.task_run_status_counts.serialize_json(
            value["task_run_status_counts"]
        )
    )
    if "task_failure_retry_count" in value:
        out["taskFailureRetryCount"] = value["task_failure_retry_count"]
    if "target_task_run_status" in value:
        import aws_sdk_deadline.types.step_target_task_run_status

        out["targetTaskRunStatus"] = (
            aws_sdk_deadline.types.step_target_task_run_status.serialize_json(
                value["target_task_run_status"]
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
    if "dependency_counts" in value:
        import aws_sdk_deadline.types.dependency_counts

        out["dependencyCounts"] = (
            aws_sdk_deadline.types.dependency_counts.serialize_json(
                value["dependency_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> StepSummary:
    out: StepSummary = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepSummary.step_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StepSummary.name required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("StepSummary.lifecycle_status required")
    if "lifecycleStatusMessage" in data:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    if "taskRunStatus" in data:
        import aws_sdk_deadline.types.task_run_status

        out["task_run_status"] = (
            aws_sdk_deadline.types.task_run_status.deserialize_json(
                data["taskRunStatus"]
            )
        )
    else:
        raise DeserializationError("StepSummary.task_run_status required")
    if "taskRunStatusCounts" in data:
        import aws_sdk_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            aws_sdk_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    else:
        raise DeserializationError("StepSummary.task_run_status_counts required")
    if "taskFailureRetryCount" in data:
        out["task_failure_retry_count"] = data["taskFailureRetryCount"]
    if "targetTaskRunStatus" in data:
        import aws_sdk_deadline.types.step_target_task_run_status

        out["target_task_run_status"] = (
            aws_sdk_deadline.types.step_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("StepSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("StepSummary.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
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
    if "dependencyCounts" in data:
        import aws_sdk_deadline.types.dependency_counts

        out["dependency_counts"] = (
            aws_sdk_deadline.types.dependency_counts.deserialize_json(
                data["dependencyCounts"]
            )
        )
    return out

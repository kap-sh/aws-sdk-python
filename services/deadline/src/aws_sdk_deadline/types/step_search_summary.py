"""Generated from Smithy shape ``com.amazonaws.deadline#StepSearchSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.parameter_space
    import aws_sdk_deadline.types.queue_id
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


class StepSearchSummary(TypedDict):
    step_id: NotRequired["aws_sdk_deadline.types.step_id.StepId"]
    """<p>The step ID.</p>"""
    job_id: NotRequired["aws_sdk_deadline.types.job_id.JobId"]
    """<p>The job ID.</p>"""
    queue_id: NotRequired["aws_sdk_deadline.types.queue_id.QueueId"]
    """<p>The queue ID.</p>"""
    name: NotRequired["aws_sdk_deadline.types.step_name.StepName"]
    """<p>The step name.</p>"""
    lifecycle_status: NotRequired[
        "aws_sdk_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    ]
    """<p>The life cycle status.</p>"""
    lifecycle_status_message: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The life cycle status message.</p>"""
    task_run_status: NotRequired["aws_sdk_deadline.types.task_run_status.TaskRunStatus"]
    """<p>The task run status for the job.</p> <ul> <li> <p> <code>PENDING</code>–pending and waiting for resources.</p> </li> <li> <p> <code>READY</code>–ready to be processed.</p> </li> <li> <p> <code>ASSIGNED</code>–assigned and will run next on a worker.</p> </li> <li> <p> <code>SCHEDULED</code>–scheduled to be run on a worker.</p> </li> <li> <p> <code>INTERRUPTING</code>–being interrupted.</p> </li> <li> <p> <code>RUNNING</code>–running on a worker.</p> </li> <li> <p> <code>SUSPENDED</code>–the task is suspended.</p> </li> <li> <p> <code>CANCELED</code>–the task has been canceled.</p> </li> <li> <p> <code>FAILED</code>–the task has failed.</p> </li> <li> <p> <code>SUCCEEDED</code>–the task has succeeded.</p> </li> </ul>"""
    target_task_run_status: NotRequired[
        "aws_sdk_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """<p>The task status to update the job's tasks to.</p>"""
    task_run_status_counts: NotRequired[
        "aws_sdk_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    ]
    """<p>The number of tasks running on the job.</p>"""
    task_failure_retry_count: NotRequired[
        "aws_sdk_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The total number of times tasks from the step failed and were retried.</p>"""
    created_at: NotRequired["aws_sdk_deadline.types.created_at.CreatedAt"]
    """<p>The date and time the resource was created.</p>"""
    created_by: NotRequired["aws_sdk_deadline.types.created_by.CreatedBy"]
    """<p>The user or system that created this resource.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    parameter_space: NotRequired[
        "aws_sdk_deadline.types.parameter_space.ParameterSpace"
    ]
    """<p>The parameters and combination expressions for the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepSearchSummary) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "lifecycle_status" in value:
        import aws_sdk_deadline.types.step_lifecycle_status

        out["lifecycleStatus"] = (
            aws_sdk_deadline.types.step_lifecycle_status.serialize_json(
                value["lifecycle_status"]
            )
        )
    if "lifecycle_status_message" in value:
        out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    if "task_run_status" in value:
        import aws_sdk_deadline.types.task_run_status

        out["taskRunStatus"] = aws_sdk_deadline.types.task_run_status.serialize_json(
            value["task_run_status"]
        )
    if "target_task_run_status" in value:
        import aws_sdk_deadline.types.step_target_task_run_status

        out["targetTaskRunStatus"] = (
            aws_sdk_deadline.types.step_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    if "task_run_status_counts" in value:
        import aws_sdk_deadline.types.task_run_status_counts

        out["taskRunStatusCounts"] = (
            aws_sdk_deadline.types.task_run_status_counts.serialize_json(
                value["task_run_status_counts"]
            )
        )
    if "task_failure_retry_count" in value:
        out["taskFailureRetryCount"] = value["task_failure_retry_count"]
    if "created_at" in value:
        import aws_sdk_deadline.types.created_at

        out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
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
    if "parameter_space" in value:
        import aws_sdk_deadline.types.parameter_space

        out["parameterSpace"] = aws_sdk_deadline.types.parameter_space.serialize_json(
            value["parameter_space"]
        )
    return out


def deserialize_json(data: dict) -> StepSearchSummary:
    out: StepSearchSummary = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    if "name" in data:
        out["name"] = data["name"]
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    if "lifecycleStatusMessage" in data:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    if "taskRunStatus" in data:
        import aws_sdk_deadline.types.task_run_status

        out["task_run_status"] = (
            aws_sdk_deadline.types.task_run_status.deserialize_json(
                data["taskRunStatus"]
            )
        )
    if "targetTaskRunStatus" in data:
        import aws_sdk_deadline.types.step_target_task_run_status

        out["target_task_run_status"] = (
            aws_sdk_deadline.types.step_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if "taskRunStatusCounts" in data:
        import aws_sdk_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            aws_sdk_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    if "taskFailureRetryCount" in data:
        out["task_failure_retry_count"] = data["taskFailureRetryCount"]
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
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
    if "parameterSpace" in data:
        import aws_sdk_deadline.types.parameter_space

        out["parameter_space"] = (
            aws_sdk_deadline.types.parameter_space.deserialize_json(
                data["parameterSpace"]
            )
        )
    return out

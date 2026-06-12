"""Generated from Smithy shape ``com.amazonaws.deadline#GetJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.attachments
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.job_description
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.job_lifecycle_status
    import aws_sdk_deadline.types.job_name
    import aws_sdk_deadline.types.job_parameters
    import aws_sdk_deadline.types.job_priority
    import aws_sdk_deadline.types.job_target_task_run_status
    import aws_sdk_deadline.types.max_failed_tasks_count
    import aws_sdk_deadline.types.max_retries_per_task
    import aws_sdk_deadline.types.max_worker_count
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.task_failure_retry_count
    import aws_sdk_deadline.types.task_run_status
    import aws_sdk_deadline.types.task_run_status_counts
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetJobResponse(TypedDict):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    name: "aws_sdk_deadline.types.job_name.JobName"
    """<p>The name of the job.</p>"""
    lifecycle_status: "aws_sdk_deadline.types.job_lifecycle_status.JobLifecycleStatus"
    """<p>The life cycle status for the job. </p>"""
    lifecycle_status_message: "aws_sdk_deadline.types.string.String"
    """<p>A message that communicates the status of the life cycle for the job.</p>"""
    priority: "aws_sdk_deadline.types.job_priority.JobPriority"
    """<p>The job priority.</p>"""
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
    task_run_status: NotRequired["aws_sdk_deadline.types.task_run_status.TaskRunStatus"]
    """<p>The task run status for the job.</p>"""
    target_task_run_status: NotRequired[
        "aws_sdk_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """<p>The task status with which the job started.</p>"""
    task_run_status_counts: NotRequired[
        "aws_sdk_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    ]
    """<p>The number of tasks running on the job.</p>"""
    task_failure_retry_count: NotRequired[
        "aws_sdk_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The total number of times tasks from the job failed and were retried.</p>"""
    storage_profile_id: NotRequired[
        "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """<p>The storage profile ID associated with the job.</p>"""
    max_failed_tasks_count: NotRequired[
        "aws_sdk_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """<p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>"""
    max_retries_per_task: NotRequired[
        "aws_sdk_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """<p>The maximum number of retries per failed tasks.</p>"""
    parameters: NotRequired["aws_sdk_deadline.types.job_parameters.JobParameters"]
    """<p>The parameters for the job.</p>"""
    attachments: NotRequired["aws_sdk_deadline.types.attachments.Attachments"]
    """<p>The attachments for the job.</p>"""
    description: NotRequired["aws_sdk_deadline.types.job_description.JobDescription"]
    """<p>The description of the job.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    max_worker_count: NotRequired[
        "aws_sdk_deadline.types.max_worker_count.MaxWorkerCount"
    ]
    """<p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>If you don't set the <code>maxWorkerCount</code> when you create a job, this value is not returned in the response.</p>"""
    source_job_id: NotRequired["aws_sdk_deadline.types.job_id.JobId"]
    """<p>The job ID for the source job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["name"] = value["name"]
    import aws_sdk_deadline.types.job_lifecycle_status

    out["lifecycleStatus"] = aws_sdk_deadline.types.job_lifecycle_status.serialize_json(
        value["lifecycle_status"]
    )
    out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    out["priority"] = value["priority"]
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
    if "task_run_status" in value:
        import aws_sdk_deadline.types.task_run_status

        out["taskRunStatus"] = aws_sdk_deadline.types.task_run_status.serialize_json(
            value["task_run_status"]
        )
    if "target_task_run_status" in value:
        import aws_sdk_deadline.types.job_target_task_run_status

        out["targetTaskRunStatus"] = (
            aws_sdk_deadline.types.job_target_task_run_status.serialize_json(
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
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "parameters" in value:
        import aws_sdk_deadline.types.job_parameters

        out["parameters"] = aws_sdk_deadline.types.job_parameters.serialize_json(
            value["parameters"]
        )
    if "attachments" in value:
        import aws_sdk_deadline.types.attachments

        out["attachments"] = aws_sdk_deadline.types.attachments.serialize_json(
            value["attachments"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "source_job_id" in value:
        out["sourceJobId"] = value["source_job_id"]
    return out


def deserialize_json(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetJobResponse.job_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetJobResponse.name required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.job_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.job_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.lifecycle_status required")
    if "lifecycleStatusMessage" in data:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    else:
        raise DeserializationError("GetJobResponse.lifecycle_status_message required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("GetJobResponse.priority required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetJobResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetJobResponse.created_by required")
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
    if "taskRunStatus" in data:
        import aws_sdk_deadline.types.task_run_status

        out["task_run_status"] = (
            aws_sdk_deadline.types.task_run_status.deserialize_json(
                data["taskRunStatus"]
            )
        )
    if "targetTaskRunStatus" in data:
        import aws_sdk_deadline.types.job_target_task_run_status

        out["target_task_run_status"] = (
            aws_sdk_deadline.types.job_target_task_run_status.deserialize_json(
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
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    if "maxFailedTasksCount" in data:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if "maxRetriesPerTask" in data:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if "parameters" in data:
        import aws_sdk_deadline.types.job_parameters

        out["parameters"] = aws_sdk_deadline.types.job_parameters.deserialize_json(
            data["parameters"]
        )
    if "attachments" in data:
        import aws_sdk_deadline.types.attachments

        out["attachments"] = aws_sdk_deadline.types.attachments.deserialize_json(
            data["attachments"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    if "sourceJobId" in data:
        out["source_job_id"] = data["sourceJobId"]
    return out

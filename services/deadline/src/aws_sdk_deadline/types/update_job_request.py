"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_description_override
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.job_name
    import aws_sdk_deadline.types.job_priority
    import aws_sdk_deadline.types.job_target_task_run_status
    import aws_sdk_deadline.types.max_failed_tasks_count
    import aws_sdk_deadline.types.max_retries_per_task
    import aws_sdk_deadline.types.max_worker_count
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.update_job_lifecycle_status


class UpdateJobRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the job to update.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the job to update.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    target_task_run_status: NotRequired[
        "aws_sdk_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """<p>The task status to update the job's tasks to.</p>"""
    priority: NotRequired["aws_sdk_deadline.types.job_priority.JobPriority"]
    """<p>The updated job priority.</p>"""
    max_failed_tasks_count: NotRequired[
        "aws_sdk_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """<p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>"""
    max_retries_per_task: NotRequired[
        "aws_sdk_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """<p>The maximum number of retries for a job.</p>"""
    lifecycle_status: NotRequired[
        "aws_sdk_deadline.types.update_job_lifecycle_status.UpdateJobLifecycleStatus"
    ]
    """<p>The status of a job in its lifecycle. When you change the status of the job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived jobs and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>"""
    max_worker_count: NotRequired[
        "aws_sdk_deadline.types.max_worker_count.MaxWorkerCount"
    ]
    """<p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, the default is -1.</p> <p>The maximum number of workers that can process tasks in the job.</p>"""
    name: NotRequired["aws_sdk_deadline.types.job_name.JobName"]
    """<p>The updated job name.</p>"""
    description: NotRequired[
        "aws_sdk_deadline.types.job_description_override.JobDescriptionOverride"
    ]
    """<p>The updated job description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobRequest) -> dict:
    out: dict = {}
    if "target_task_run_status" in value:
        import aws_sdk_deadline.types.job_target_task_run_status

        out["targetTaskRunStatus"] = (
            aws_sdk_deadline.types.job_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "lifecycle_status" in value:
        import aws_sdk_deadline.types.update_job_lifecycle_status

        out["lifecycleStatus"] = (
            aws_sdk_deadline.types.update_job_lifecycle_status.serialize_json(
                value["lifecycle_status"]
            )
        )
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "targetTaskRunStatus" in data:
        import aws_sdk_deadline.types.job_target_task_run_status

        out["target_task_run_status"] = (
            aws_sdk_deadline.types.job_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "maxFailedTasksCount" in data:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if "maxRetriesPerTask" in data:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.update_job_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.update_job_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out

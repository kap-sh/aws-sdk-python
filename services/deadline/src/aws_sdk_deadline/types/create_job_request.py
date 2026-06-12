"""Generated from Smithy shape ``com.amazonaws.deadline#CreateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.attachments
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.create_job_target_task_run_status
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_description_override
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.job_name
    import aws_sdk_deadline.types.job_parameters
    import aws_sdk_deadline.types.job_priority
    import aws_sdk_deadline.types.job_template
    import aws_sdk_deadline.types.job_template_type
    import aws_sdk_deadline.types.max_failed_tasks_count
    import aws_sdk_deadline.types.max_retries_per_task
    import aws_sdk_deadline.types.max_worker_count
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.tags


class CreateJobRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the job.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The ID of the queue that the job is submitted to.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    template: NotRequired["aws_sdk_deadline.types.job_template.JobTemplate"]
    """<p>The job template to use for this job.</p>"""
    template_type: NotRequired[
        "aws_sdk_deadline.types.job_template_type.JobTemplateType"
    ]
    """<p>The file type for the job template.</p>"""
    priority: "aws_sdk_deadline.types.job_priority.JobPriority"
    """<p>The priority of the job. The highest priority (first scheduled) is 100. When two jobs have the same priority, the oldest job is scheduled first.</p>"""
    parameters: NotRequired["aws_sdk_deadline.types.job_parameters.JobParameters"]
    """<p>The parameters for the job.</p>"""
    attachments: NotRequired["aws_sdk_deadline.types.attachments.Attachments"]
    """<p>The attachments for the job. Attach files required for the job to run to a render job.</p>"""
    storage_profile_id: NotRequired[
        "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """<p>The storage profile ID for the storage profile to connect to the job.</p>"""
    target_task_run_status: "aws_sdk_deadline.types.create_job_target_task_run_status.CreateJobTargetTaskRunStatus"
    """<p>The initial job status when it is created. Jobs that are created with a <code>SUSPENDED</code> status will not run until manually requeued.</p>"""
    max_failed_tasks_count: (
        "aws_sdk_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    )
    """<p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>"""
    max_retries_per_task: (
        "aws_sdk_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    )
    """<p>The maximum number of retries for each task.</p>"""
    max_worker_count: NotRequired[
        "aws_sdk_deadline.types.max_worker_count.MaxWorkerCount"
    ]
    """<p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, Deadline Cloud won't throttle the number of workers used to process the job.</p>"""
    source_job_id: NotRequired["aws_sdk_deadline.types.job_id.JobId"]
    """<p>The job ID for the source job.</p>"""
    name_override: NotRequired["aws_sdk_deadline.types.job_name.JobName"]
    """<p>A custom name to override the job name derived from the job template.</p>"""
    description_override: NotRequired[
        "aws_sdk_deadline.types.job_description_override.JobDescriptionOverride"
    ]
    """<p>A custom description to override the job description derived from the job template.</p>"""
    tags: NotRequired["aws_sdk_deadline.types.tags.Tags"]
    """<p>The tags to add to your job. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "template" in value:
        out["template"] = value["template"]
    if "template_type" in value:
        import aws_sdk_deadline.types.job_template_type

        out["templateType"] = aws_sdk_deadline.types.job_template_type.serialize_json(
            value["template_type"]
        )
    out["priority"] = value["priority"]
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
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    import aws_sdk_deadline.types.create_job_target_task_run_status

    out["targetTaskRunStatus"] = (
        aws_sdk_deadline.types.create_job_target_task_run_status.serialize_json(
            value.get("target_task_run_status", "READY")
        )
    )
    out["maxFailedTasksCount"] = value.get("max_failed_tasks_count", 20)
    out["maxRetriesPerTask"] = value.get("max_retries_per_task", 5)
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "source_job_id" in value:
        out["sourceJobId"] = value["source_job_id"]
    if "name_override" in value:
        out["nameOverride"] = value["name_override"]
    if "description_override" in value:
        out["descriptionOverride"] = value["description_override"]
    if "tags" in value:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if "template" in data:
        out["template"] = data["template"]
    if "templateType" in data:
        import aws_sdk_deadline.types.job_template_type

        out["template_type"] = (
            aws_sdk_deadline.types.job_template_type.deserialize_json(
                data["templateType"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateJobRequest.priority required")
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
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    if "targetTaskRunStatus" in data:
        import aws_sdk_deadline.types.create_job_target_task_run_status

        out["target_task_run_status"] = (
            aws_sdk_deadline.types.create_job_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    else:
        out["target_task_run_status"] = "READY"
    if "maxFailedTasksCount" in data:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    else:
        out["max_failed_tasks_count"] = 20
    if "maxRetriesPerTask" in data:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    else:
        out["max_retries_per_task"] = 5
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    if "sourceJobId" in data:
        out["source_job_id"] = data["sourceJobId"]
    if "nameOverride" in data:
        out["name_override"] = data["nameOverride"]
    if "descriptionOverride" in data:
        out["description_override"] = data["descriptionOverride"]
    if "tags" in data:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.deserialize_json(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.dependency_counts
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.parameter_space
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.step_description
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.step_lifecycle_status
    import aws_sdk_deadline.types.step_name
    import aws_sdk_deadline.types.step_required_capabilities
    import aws_sdk_deadline.types.step_target_task_run_status
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.task_failure_retry_count
    import aws_sdk_deadline.types.task_run_status
    import aws_sdk_deadline.types.task_run_status_counts
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class BatchGetStepItem(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the step.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the step.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the step.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    name: "aws_sdk_deadline.types.step_name.StepName"
    """<p>The name of the step.</p>"""
    lifecycle_status: "aws_sdk_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    """<p>The life cycle status of the step.</p>"""
    lifecycle_status_message: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>A message that communicates the status of the life cycle.</p>"""
    task_run_status: "aws_sdk_deadline.types.task_run_status.TaskRunStatus"
    """<p>The task run status for the step.</p>"""
    task_run_status_counts: (
        "aws_sdk_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    )
    """<p>The number of tasks for each run status for the step.</p>"""
    task_failure_retry_count: NotRequired[
        "aws_sdk_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The number of times that tasks failed and were retried.</p>"""
    target_task_run_status: NotRequired[
        "aws_sdk_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """<p>The task status to start with on the step.</p>"""
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
    required_capabilities: NotRequired[
        "aws_sdk_deadline.types.step_required_capabilities.StepRequiredCapabilities"
    ]
    """<p>The required capabilities for the step.</p>"""
    parameter_space: NotRequired[
        "aws_sdk_deadline.types.parameter_space.ParameterSpace"
    ]
    """<p>The parameter space for the step.</p>"""
    description: NotRequired["aws_sdk_deadline.types.step_description.StepDescription"]
    """<p>The description of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
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
    if "required_capabilities" in value:
        import aws_sdk_deadline.types.step_required_capabilities

        out["requiredCapabilities"] = (
            aws_sdk_deadline.types.step_required_capabilities.serialize_json(
                value["required_capabilities"]
            )
        )
    if "parameter_space" in value:
        import aws_sdk_deadline.types.parameter_space

        out["parameterSpace"] = aws_sdk_deadline.types.parameter_space.serialize_json(
            value["parameter_space"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BatchGetStepItem:
    out: BatchGetStepItem = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetStepItem.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetStepItem.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetStepItem.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchGetStepItem.step_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchGetStepItem.name required")
    if "lifecycleStatus" in data:
        import aws_sdk_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            aws_sdk_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("BatchGetStepItem.lifecycle_status required")
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
        raise DeserializationError("BatchGetStepItem.task_run_status required")
    if "taskRunStatusCounts" in data:
        import aws_sdk_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            aws_sdk_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    else:
        raise DeserializationError("BatchGetStepItem.task_run_status_counts required")
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
        raise DeserializationError("BatchGetStepItem.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("BatchGetStepItem.created_by required")
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
    if "requiredCapabilities" in data:
        import aws_sdk_deadline.types.step_required_capabilities

        out["required_capabilities"] = (
            aws_sdk_deadline.types.step_required_capabilities.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    if "parameterSpace" in data:
        import aws_sdk_deadline.types.parameter_space

        out["parameter_space"] = (
            aws_sdk_deadline.types.parameter_space.deserialize_json(
                data["parameterSpace"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out

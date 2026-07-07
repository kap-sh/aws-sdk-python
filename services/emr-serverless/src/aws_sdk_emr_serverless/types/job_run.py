"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.attempt_number
    import aws_sdk_emr_serverless.types.configuration_overrides
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.duration
    import aws_sdk_emr_serverless.types.iam_role_arn
    import aws_sdk_emr_serverless.types.image_configuration
    import aws_sdk_emr_serverless.types.job_arn
    import aws_sdk_emr_serverless.types.job_driver
    import aws_sdk_emr_serverless.types.job_run_execution_iam_policy
    import aws_sdk_emr_serverless.types.job_run_id
    import aws_sdk_emr_serverless.types.job_run_mode
    import aws_sdk_emr_serverless.types.job_run_state
    import aws_sdk_emr_serverless.types.network_configuration
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.request_identity_user_arn
    import aws_sdk_emr_serverless.types.resource_utilization
    import aws_sdk_emr_serverless.types.retry_policy
    import aws_sdk_emr_serverless.types.string256
    import aws_sdk_emr_serverless.types.tag_map
    import aws_sdk_emr_serverless.types.total_resource_utilization
    import aws_sdk_emr_serverless.types.worker_type_specification_map


class JobRun(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application the job is running on.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The optional job run name. This doesn't have to be unique.</p>"""
    arn: "aws_sdk_emr_serverless.types.job_arn.JobArn"
    """<p>The execution role ARN of the job run.</p>"""
    created_by: (
        "aws_sdk_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The user who created the job run.</p>"""
    created_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the job run was created.</p>"""
    updated_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the job run was updated.</p>"""
    execution_role: "aws_sdk_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The execution role ARN of the job run.</p>"""
    execution_iam_policy: NotRequired[
        "aws_sdk_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
    ]
    state: "aws_sdk_emr_serverless.types.job_run_state.JobRunState"
    """<p>The state of the job run.</p>"""
    state_details: "aws_sdk_emr_serverless.types.string256.String256"
    """<p>The state details of the job run.</p>"""
    release_label: "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release associated with the application your job is running on.</p>"""
    configuration_overrides: NotRequired[
        "aws_sdk_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration settings that are used to override default configuration.</p>"""
    job_driver: "aws_sdk_emr_serverless.types.job_driver.JobDriver"
    """<p>The job driver for the job run.</p>"""
    tags: NotRequired["aws_sdk_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the job run.</p>"""
    total_resource_utilization: NotRequired[
        "aws_sdk_emr_serverless.types.total_resource_utilization.TotalResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage resources used from the time the job starts to execute, until the time the job terminates, rounded up to the nearest second.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.network_configuration.NetworkConfiguration"
    ]
    total_execution_duration_seconds: NotRequired["int"]
    """<p>The job run total execution duration in seconds. This field is only available for job runs in a <code>COMPLETED</code>, <code>FAILED</code>, or <code>CANCELLED</code> state.</p>"""
    execution_timeout_minutes: NotRequired[
        "aws_sdk_emr_serverless.types.duration.Duration"
    ]
    """<p>Returns the job run timeout value from the <code>StartJobRun</code> call. If no timeout was specified, then it returns the default timeout of 720 minutes.</p>"""
    billed_resource_utilization: NotRequired[
        "aws_sdk_emr_serverless.types.resource_utilization.ResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage that Amazon Web Services has billed for the job run. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker. Note that billed resources do not include usage for idle pre-initialized workers.</p>"""
    mode: NotRequired["aws_sdk_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run.</p>"""
    retry_policy: NotRequired["aws_sdk_emr_serverless.types.retry_policy.RetryPolicy"]
    """<p>The retry policy of the job run.</p>"""
    attempt: NotRequired["aws_sdk_emr_serverless.types.attempt_number.AttemptNumber"]
    """<p>The attempt of the job run.</p>"""
    attempt_created_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time of when the job run attempt was created.</p>"""
    attempt_updated_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time of when the job run attempt was last updated.</p>"""
    started_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time when the job moved to the RUNNING state.</p>"""
    ended_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time when the job was terminated.</p>"""
    queued_duration_milliseconds: NotRequired["int"]
    """<p>The total time for a job in the QUEUED state in milliseconds.</p>"""
    image_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.image_configuration.ImageConfiguration"
    ]
    worker_type_specifications: NotRequired[
        "aws_sdk_emr_serverless.types.worker_type_specification_map.WorkerTypeSpecificationMap"
    ]
    """<p>The specification applied to each worker type. Includes the JobRun-level ImageConfiguration when the applicationLevelDigestResolution is false for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRun) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["jobRunId"] = value["job_run_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["createdBy"] = value["created_by"]
    import aws_sdk_emr_serverless.types.date

    out["createdAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import aws_sdk_emr_serverless.types.date

    out["updatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    out["executionRole"] = value["execution_role"]
    if "execution_iam_policy" in value:
        import aws_sdk_emr_serverless.types.job_run_execution_iam_policy

        out["executionIamPolicy"] = (
            aws_sdk_emr_serverless.types.job_run_execution_iam_policy.serialize_json(
                value["execution_iam_policy"]
            )
        )
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    if "configuration_overrides" in value:
        import aws_sdk_emr_serverless.types.configuration_overrides

        out["configurationOverrides"] = (
            aws_sdk_emr_serverless.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    import aws_sdk_emr_serverless.types.job_driver

    out["jobDriver"] = aws_sdk_emr_serverless.types.job_driver.serialize_json(
        value["job_driver"]
    )
    if "tags" in value:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "total_resource_utilization" in value:
        import aws_sdk_emr_serverless.types.total_resource_utilization

        out["totalResourceUtilization"] = (
            aws_sdk_emr_serverless.types.total_resource_utilization.serialize_json(
                value["total_resource_utilization"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_emr_serverless.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_emr_serverless.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "total_execution_duration_seconds" in value:
        out["totalExecutionDurationSeconds"] = value["total_execution_duration_seconds"]
    if "execution_timeout_minutes" in value:
        out["executionTimeoutMinutes"] = value["execution_timeout_minutes"]
    if "billed_resource_utilization" in value:
        import aws_sdk_emr_serverless.types.resource_utilization

        out["billedResourceUtilization"] = (
            aws_sdk_emr_serverless.types.resource_utilization.serialize_json(
                value["billed_resource_utilization"]
            )
        )
    if "mode" in value:
        out["mode"] = value["mode"]
    if "retry_policy" in value:
        import aws_sdk_emr_serverless.types.retry_policy

        out["retryPolicy"] = aws_sdk_emr_serverless.types.retry_policy.serialize_json(
            value["retry_policy"]
        )
    if "attempt" in value:
        out["attempt"] = value["attempt"]
    if "attempt_created_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["attemptCreatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["attempt_created_at"]
        )
    if "attempt_updated_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["attemptUpdatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["attempt_updated_at"]
        )
    if "started_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["startedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["endedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["ended_at"]
        )
    if "queued_duration_milliseconds" in value:
        out["queuedDurationMilliseconds"] = value["queued_duration_milliseconds"]
    if "image_configuration" in value:
        import aws_sdk_emr_serverless.types.image_configuration

        out["imageConfiguration"] = (
            aws_sdk_emr_serverless.types.image_configuration.serialize_json(
                value["image_configuration"]
            )
        )
    if "worker_type_specifications" in value:
        import aws_sdk_emr_serverless.types.worker_type_specification_map

        out["workerTypeSpecifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_map.serialize_json(
                value["worker_type_specifications"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobRun:
    out: JobRun = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("JobRun.application_id required")
    if "jobRunId" in data:
        out["job_run_id"] = data["jobRunId"]
    else:
        raise DeserializationError("JobRun.job_run_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("JobRun.arn required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("JobRun.created_by required")
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("JobRun.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("JobRun.updated_at required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("JobRun.execution_role required")
    if "executionIamPolicy" in data:
        import aws_sdk_emr_serverless.types.job_run_execution_iam_policy

        out["execution_iam_policy"] = (
            aws_sdk_emr_serverless.types.job_run_execution_iam_policy.deserialize_json(
                data["executionIamPolicy"]
            )
        )
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("JobRun.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    else:
        raise DeserializationError("JobRun.state_details required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("JobRun.release_label required")
    if "configurationOverrides" in data:
        import aws_sdk_emr_serverless.types.configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_emr_serverless.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if "jobDriver" in data:
        import aws_sdk_emr_serverless.types.job_driver

        out["job_driver"] = aws_sdk_emr_serverless.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    else:
        raise DeserializationError("JobRun.job_driver required")
    if "tags" in data:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "totalResourceUtilization" in data:
        import aws_sdk_emr_serverless.types.total_resource_utilization

        out["total_resource_utilization"] = (
            aws_sdk_emr_serverless.types.total_resource_utilization.deserialize_json(
                data["totalResourceUtilization"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_emr_serverless.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_emr_serverless.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "totalExecutionDurationSeconds" in data:
        out["total_execution_duration_seconds"] = data["totalExecutionDurationSeconds"]
    if "executionTimeoutMinutes" in data:
        out["execution_timeout_minutes"] = data["executionTimeoutMinutes"]
    if "billedResourceUtilization" in data:
        import aws_sdk_emr_serverless.types.resource_utilization

        out["billed_resource_utilization"] = (
            aws_sdk_emr_serverless.types.resource_utilization.deserialize_json(
                data["billedResourceUtilization"]
            )
        )
    if "mode" in data:
        out["mode"] = data["mode"]
    if "retryPolicy" in data:
        import aws_sdk_emr_serverless.types.retry_policy

        out["retry_policy"] = (
            aws_sdk_emr_serverless.types.retry_policy.deserialize_json(
                data["retryPolicy"]
            )
        )
    if "attempt" in data:
        out["attempt"] = data["attempt"]
    if "attemptCreatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["attempt_created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["attemptCreatedAt"]
        )
    if "attemptUpdatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["attempt_updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["attemptUpdatedAt"]
        )
    if "startedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["started_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["ended_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["endedAt"]
        )
    if "queuedDurationMilliseconds" in data:
        out["queued_duration_milliseconds"] = data["queuedDurationMilliseconds"]
    if "imageConfiguration" in data:
        import aws_sdk_emr_serverless.types.image_configuration

        out["image_configuration"] = (
            aws_sdk_emr_serverless.types.image_configuration.deserialize_json(
                data["imageConfiguration"]
            )
        )
    if "workerTypeSpecifications" in data:
        import aws_sdk_emr_serverless.types.worker_type_specification_map

        out["worker_type_specifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_map.deserialize_json(
                data["workerTypeSpecifications"]
            )
        )
    return out

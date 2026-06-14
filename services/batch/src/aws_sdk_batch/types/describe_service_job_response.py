"""Generated from Smithy shape ``com.amazonaws.batch#DescribeServiceJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.latest_service_job_attempt
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.service_job_attempt_details
    import aws_sdk_batch.types.service_job_capacity_usage_detail_list
    import aws_sdk_batch.types.service_job_preemption_configuration
    import aws_sdk_batch.types.service_job_preemption_summary
    import aws_sdk_batch.types.service_job_retry_strategy
    import aws_sdk_batch.types.service_job_status
    import aws_sdk_batch.types.service_job_timeout
    import aws_sdk_batch.types.service_job_type
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class DescribeServiceJobResponse(TypedDict):
    attempts: NotRequired[
        "aws_sdk_batch.types.service_job_attempt_details.ServiceJobAttemptDetails"
    ]
    """<p>A list of job attempts associated with the service job.</p>"""
    capacity_usage: NotRequired[
        "aws_sdk_batch.types.service_job_capacity_usage_detail_list.ServiceJobCapacityUsageDetailList"
    ]
    """<p>The configured capacity for the service job, such as the number of instances. The number of instances should be the same value as the <code>serviceRequestPayload.InstanceCount</code> field.</p>"""
    created_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was created.</p>"""
    is_terminated: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Indicates whether the service job has been terminated.</p>"""
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service job.</p>"""
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job ID for the service job.</p>"""
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the service job.</p>"""
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The ARN of the job queue that the service job is associated with.</p>"""
    latest_attempt: NotRequired[
        "aws_sdk_batch.types.latest_service_job_attempt.LatestServiceJobAttempt"
    ]
    """<p>The latest attempt associated with the service job.</p>"""
    retry_strategy: NotRequired[
        "aws_sdk_batch.types.service_job_retry_strategy.ServiceJobRetryStrategy"
    ]
    """<p>The retry strategy to use for failed service jobs that are submitted with this service job.</p>"""
    scheduled_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was scheduled. This represents when the service job was dispatched to SageMaker and the service job transitioned to the <code>SCHEDULED</code> state.</p>"""
    scheduling_priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The scheduling priority of the service job. </p>"""
    service_request_payload: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The request, in JSON, for the service that the <code>SubmitServiceJob</code> operation is queueing. </p>"""
    service_job_type: NotRequired["aws_sdk_batch.types.service_job_type.ServiceJobType"]
    """<p>The type of service job. For SageMaker Training jobs, this value is <code>SAGEMAKER_TRAINING</code>.</p>"""
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The share identifier for the service job. This is used for fair-share scheduling.</p>"""
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the quota share that the service job is associated with.</p>"""
    preemption_configuration: NotRequired[
        "aws_sdk_batch.types.service_job_preemption_configuration.ServiceJobPreemptionConfiguration"
    ]
    """<p>Specifies the service job behavior when preempted.</p>"""
    preemption_summary: NotRequired[
        "aws_sdk_batch.types.service_job_preemption_summary.ServiceJobPreemptionSummary"
    ]
    """<p>Summarizes the preemptions of the service job. This field appears on a service job when it has been preempted.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was started.</p>"""
    status: NotRequired["aws_sdk_batch.types.service_job_status.ServiceJobStatus"]
    """<p>The current status of the service job. </p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the service job.</p>"""
    stopped_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job stopped running.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags that are associated with the service job. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""
    timeout_config: NotRequired[
        "aws_sdk_batch.types.service_job_timeout.ServiceJobTimeout"
    ]
    """<p>The timeout configuration for the service job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeServiceJobResponse) -> dict:
    out: dict = {}
    if "attempts" in value:
        import aws_sdk_batch.types.service_job_attempt_details

        out["attempts"] = (
            aws_sdk_batch.types.service_job_attempt_details.serialize_json(
                value["attempts"]
            )
        )
    if "capacity_usage" in value:
        import aws_sdk_batch.types.service_job_capacity_usage_detail_list

        out["capacityUsage"] = (
            aws_sdk_batch.types.service_job_capacity_usage_detail_list.serialize_json(
                value["capacity_usage"]
            )
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "is_terminated" in value:
        out["isTerminated"] = value["is_terminated"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "latest_attempt" in value:
        import aws_sdk_batch.types.latest_service_job_attempt

        out["latestAttempt"] = (
            aws_sdk_batch.types.latest_service_job_attempt.serialize_json(
                value["latest_attempt"]
            )
        )
    if "retry_strategy" in value:
        import aws_sdk_batch.types.service_job_retry_strategy

        out["retryStrategy"] = (
            aws_sdk_batch.types.service_job_retry_strategy.serialize_json(
                value["retry_strategy"]
            )
        )
    if "scheduled_at" in value:
        out["scheduledAt"] = value["scheduled_at"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "service_request_payload" in value:
        out["serviceRequestPayload"] = value["service_request_payload"]
    if "service_job_type" in value:
        import aws_sdk_batch.types.service_job_type

        out["serviceJobType"] = aws_sdk_batch.types.service_job_type.serialize_json(
            value["service_job_type"]
        )
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "preemption_configuration" in value:
        import aws_sdk_batch.types.service_job_preemption_configuration

        out["preemptionConfiguration"] = (
            aws_sdk_batch.types.service_job_preemption_configuration.serialize_json(
                value["preemption_configuration"]
            )
        )
    if "preemption_summary" in value:
        import aws_sdk_batch.types.service_job_preemption_summary

        out["preemptionSummary"] = (
            aws_sdk_batch.types.service_job_preemption_summary.serialize_json(
                value["preemption_summary"]
            )
        )
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "status" in value:
        import aws_sdk_batch.types.service_job_status

        out["status"] = aws_sdk_batch.types.service_job_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "timeout_config" in value:
        import aws_sdk_batch.types.service_job_timeout

        out["timeoutConfig"] = aws_sdk_batch.types.service_job_timeout.serialize_json(
            value["timeout_config"]
        )
    return out


def deserialize_json(data: dict) -> DescribeServiceJobResponse:
    out: DescribeServiceJobResponse = {}  # type: ignore[typeddict-item]
    if "attempts" in data:
        import aws_sdk_batch.types.service_job_attempt_details

        out["attempts"] = (
            aws_sdk_batch.types.service_job_attempt_details.deserialize_json(
                data["attempts"]
            )
        )
    if "capacityUsage" in data:
        import aws_sdk_batch.types.service_job_capacity_usage_detail_list

        out["capacity_usage"] = (
            aws_sdk_batch.types.service_job_capacity_usage_detail_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "isTerminated" in data:
        out["is_terminated"] = data["isTerminated"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "latestAttempt" in data:
        import aws_sdk_batch.types.latest_service_job_attempt

        out["latest_attempt"] = (
            aws_sdk_batch.types.latest_service_job_attempt.deserialize_json(
                data["latestAttempt"]
            )
        )
    if "retryStrategy" in data:
        import aws_sdk_batch.types.service_job_retry_strategy

        out["retry_strategy"] = (
            aws_sdk_batch.types.service_job_retry_strategy.deserialize_json(
                data["retryStrategy"]
            )
        )
    if "scheduledAt" in data:
        out["scheduled_at"] = data["scheduledAt"]
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    if "serviceRequestPayload" in data:
        out["service_request_payload"] = data["serviceRequestPayload"]
    if "serviceJobType" in data:
        import aws_sdk_batch.types.service_job_type

        out["service_job_type"] = aws_sdk_batch.types.service_job_type.deserialize_json(
            data["serviceJobType"]
        )
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "preemptionConfiguration" in data:
        import aws_sdk_batch.types.service_job_preemption_configuration

        out["preemption_configuration"] = (
            aws_sdk_batch.types.service_job_preemption_configuration.deserialize_json(
                data["preemptionConfiguration"]
            )
        )
    if "preemptionSummary" in data:
        import aws_sdk_batch.types.service_job_preemption_summary

        out["preemption_summary"] = (
            aws_sdk_batch.types.service_job_preemption_summary.deserialize_json(
                data["preemptionSummary"]
            )
        )
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "status" in data:
        import aws_sdk_batch.types.service_job_status

        out["status"] = aws_sdk_batch.types.service_job_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if "timeoutConfig" in data:
        import aws_sdk_batch.types.service_job_timeout

        out["timeout_config"] = (
            aws_sdk_batch.types.service_job_timeout.deserialize_json(
                data["timeoutConfig"]
            )
        )
    return out

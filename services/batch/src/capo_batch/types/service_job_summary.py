"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.latest_service_job_attempt
    import capo_batch.types.long
    import capo_batch.types.service_job_capacity_usage_summary_list
    import capo_batch.types.service_job_status
    import capo_batch.types.service_job_type
    import capo_batch.types.string


class ServiceJobSummary(TypedDict, closed=True):
    latest_attempt: NotRequired[
        "capo_batch.types.latest_service_job_attempt.LatestServiceJobAttempt"
    ]
    """<p>Information about the latest attempt for the service job.</p>"""
    capacity_usage: NotRequired[
        "capo_batch.types.service_job_capacity_usage_summary_list.ServiceJobCapacityUsageSummaryList"
    ]
    """<p>The capacity usage information for this service job, including the unit of measure and quantity of resources being used.</p>"""
    created_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was created.</p>"""
    job_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service job.</p>"""
    job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The job ID for the service job.</p>"""
    job_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the service job.</p>"""
    scheduled_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was scheduled for execution.</p>"""
    service_job_type: NotRequired["capo_batch.types.service_job_type.ServiceJobType"]
    """<p>The type of service job. For SageMaker Training jobs, this value is <code>SAGEMAKER_TRAINING</code>.</p>"""
    share_identifier: NotRequired["capo_batch.types.string.String"]
    """<p>The share identifier for the job.</p>"""
    quota_share_name: NotRequired["capo_batch.types.string.String"]
    """<p>The quota share for the service job.</p>"""
    status: NotRequired["capo_batch.types.service_job_status.ServiceJobStatus"]
    """<p>The current status of the service job. </p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short string to provide more details on the current status of the service job.</p>"""
    started_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job was started.</p>"""
    stopped_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job stopped running.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobSummary) -> dict:
    out: dict = {}
    if "latest_attempt" in value:
        import capo_batch.types.latest_service_job_attempt

        out["latestAttempt"] = (
            capo_batch.types.latest_service_job_attempt.serialize_json(
                value["latest_attempt"]
            )
        )
    if "capacity_usage" in value:
        import capo_batch.types.service_job_capacity_usage_summary_list

        out["capacityUsage"] = (
            capo_batch.types.service_job_capacity_usage_summary_list.serialize_json(
                value["capacity_usage"]
            )
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "scheduled_at" in value:
        out["scheduledAt"] = value["scheduled_at"]
    if "service_job_type" in value:
        import capo_batch.types.service_job_type

        out["serviceJobType"] = capo_batch.types.service_job_type.serialize_json(
            value["service_job_type"]
        )
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "status" in value:
        import capo_batch.types.service_job_status

        out["status"] = capo_batch.types.service_job_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    return out


def deserialize_json(data: dict) -> ServiceJobSummary:
    out: ServiceJobSummary = {}  # type: ignore[typeddict-item]
    if "latestAttempt" in data:
        import capo_batch.types.latest_service_job_attempt

        out["latest_attempt"] = (
            capo_batch.types.latest_service_job_attempt.deserialize_json(
                data["latestAttempt"]
            )
        )
    if "capacityUsage" in data:
        import capo_batch.types.service_job_capacity_usage_summary_list

        out["capacity_usage"] = (
            capo_batch.types.service_job_capacity_usage_summary_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "scheduledAt" in data:
        out["scheduled_at"] = data["scheduledAt"]
    if "serviceJobType" in data:
        import capo_batch.types.service_job_type

        out["service_job_type"] = capo_batch.types.service_job_type.deserialize_json(
            data["serviceJobType"]
        )
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "status" in data:
        import capo_batch.types.service_job_status

        out["status"] = capo_batch.types.service_job_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    return out

"""Generated from Smithy shape ``com.amazonaws.batch#JobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.array_properties_summary
    import aws_sdk_batch.types.container_summary
    import aws_sdk_batch.types.job_capacity_usage_summary_list
    import aws_sdk_batch.types.job_status
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.node_properties_summary
    import aws_sdk_batch.types.string


class JobSummary(TypedDict):
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job ID.</p>"""
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job name.</p>"""
    capacity_usage: NotRequired[
        "aws_sdk_batch.types.job_capacity_usage_summary_list.JobCapacityUsageSummaryList"
    ]
    """<p>The configured capacity usage information for this job, including the unit of measure and quantity of resources.</p>"""
    created_at: NotRequired["aws_sdk_batch.types.long.Long"]
    r"""<p>The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the <code>SUBMITTED</code> state (at the time <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html\">SubmitJob</a> was called). For array child jobs, this is when the child job was spawned by its parent and entered the <code>PENDING</code> state.</p>"""
    scheduled_at: NotRequired["aws_sdk_batch.types.long.Long"]
    r"""<p>The Unix timestamp (in milliseconds) for when the job was scheduled for execution. For more information on job statues, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/service-job-status.html\">Service job status</a> in the <i>Batch User Guide</i>.</p>"""
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The share identifier for the fairshare scheduling queue that this job is associated with.</p>"""
    status: NotRequired["aws_sdk_batch.types.job_status.JobStatus"]
    """<p>The current status for the job.</p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state.</p>"""
    stopped_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was stopped. More specifically, it's when the job transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>.</p>"""
    container: NotRequired["aws_sdk_batch.types.container_summary.ContainerSummary"]
    """<p>An object that represents the details of the container that's associated with the job.</p>"""
    array_properties: NotRequired[
        "aws_sdk_batch.types.array_properties_summary.ArrayPropertiesSummary"
    ]
    """<p>The array properties of the job, if it's an array job.</p>"""
    node_properties: NotRequired[
        "aws_sdk_batch.types.node_properties_summary.NodePropertiesSummary"
    ]
    """<p>The node properties for a single node in a job summary list.</p> <note> <p>This isn't applicable to jobs that are running on Fargate resources.</p> </note>"""
    job_definition: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "capacity_usage" in value:
        import aws_sdk_batch.types.job_capacity_usage_summary_list

        out["capacityUsage"] = (
            aws_sdk_batch.types.job_capacity_usage_summary_list.serialize_json(
                value["capacity_usage"]
            )
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "scheduled_at" in value:
        out["scheduledAt"] = value["scheduled_at"]
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "status" in value:
        import aws_sdk_batch.types.job_status

        out["status"] = aws_sdk_batch.types.job_status.serialize_json(value["status"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "container" in value:
        import aws_sdk_batch.types.container_summary

        out["container"] = aws_sdk_batch.types.container_summary.serialize_json(
            value["container"]
        )
    if "array_properties" in value:
        import aws_sdk_batch.types.array_properties_summary

        out["arrayProperties"] = (
            aws_sdk_batch.types.array_properties_summary.serialize_json(
                value["array_properties"]
            )
        )
    if "node_properties" in value:
        import aws_sdk_batch.types.node_properties_summary

        out["nodeProperties"] = (
            aws_sdk_batch.types.node_properties_summary.serialize_json(
                value["node_properties"]
            )
        )
    if "job_definition" in value:
        out["jobDefinition"] = value["job_definition"]
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "capacityUsage" in data:
        import aws_sdk_batch.types.job_capacity_usage_summary_list

        out["capacity_usage"] = (
            aws_sdk_batch.types.job_capacity_usage_summary_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "scheduledAt" in data:
        out["scheduled_at"] = data["scheduledAt"]
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "status" in data:
        import aws_sdk_batch.types.job_status

        out["status"] = aws_sdk_batch.types.job_status.deserialize_json(data["status"])
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "container" in data:
        import aws_sdk_batch.types.container_summary

        out["container"] = aws_sdk_batch.types.container_summary.deserialize_json(
            data["container"]
        )
    if "arrayProperties" in data:
        import aws_sdk_batch.types.array_properties_summary

        out["array_properties"] = (
            aws_sdk_batch.types.array_properties_summary.deserialize_json(
                data["arrayProperties"]
            )
        )
    if "nodeProperties" in data:
        import aws_sdk_batch.types.node_properties_summary

        out["node_properties"] = (
            aws_sdk_batch.types.node_properties_summary.deserialize_json(
                data["nodeProperties"]
            )
        )
    if "jobDefinition" in data:
        out["job_definition"] = data["jobDefinition"]
    return out

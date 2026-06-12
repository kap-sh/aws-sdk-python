"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecutionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.execution_number
    import aws_sdk_iot_jobs_data_plane.types.job_id
    import aws_sdk_iot_jobs_data_plane.types.last_updated_at
    import aws_sdk_iot_jobs_data_plane.types.queued_at
    import aws_sdk_iot_jobs_data_plane.types.started_at
    import aws_sdk_iot_jobs_data_plane.types.version_number


class JobExecutionSummary(TypedDict):
    job_id: NotRequired["aws_sdk_iot_jobs_data_plane.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    queued_at: "aws_sdk_iot_jobs_data_plane.types.queued_at.QueuedAt"
    """<p>The time, in seconds since the epoch, when the job execution was enqueued.</p>"""
    started_at: NotRequired["aws_sdk_iot_jobs_data_plane.types.started_at.StartedAt"]
    """<p>The time, in seconds since the epoch, when the job execution started.</p>"""
    last_updated_at: "aws_sdk_iot_jobs_data_plane.types.last_updated_at.LastUpdatedAt"
    """<p>The time, in seconds since the epoch, when the job execution was last updated.</p>"""
    version_number: "aws_sdk_iot_jobs_data_plane.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time IoT Jobs receives an update from a device.</p>"""
    execution_number: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
    ]
    """<p>A number that identifies a particular job execution on a particular device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    out["queuedAt"] = value.get("queued_at", 0)
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    out["lastUpdatedAt"] = value.get("last_updated_at", 0)
    out["versionNumber"] = value.get("version_number", 0)
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    return out


def deserialize_json(data: dict) -> JobExecutionSummary:
    out: JobExecutionSummary = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "queuedAt" in data:
        out["queued_at"] = data["queuedAt"]
    else:
        out["queued_at"] = 0
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "lastUpdatedAt" in data:
        out["last_updated_at"] = data["lastUpdatedAt"]
    else:
        out["last_updated_at"] = 0
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    if "executionNumber" in data:
        out["execution_number"] = data["executionNumber"]
    return out

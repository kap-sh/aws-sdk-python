"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.approximate_seconds_before_timed_out
    import aws_sdk_iot_jobs_data_plane.types.details_map
    import aws_sdk_iot_jobs_data_plane.types.execution_number
    import aws_sdk_iot_jobs_data_plane.types.job_document
    import aws_sdk_iot_jobs_data_plane.types.job_execution_status
    import aws_sdk_iot_jobs_data_plane.types.job_id
    import aws_sdk_iot_jobs_data_plane.types.last_updated_at
    import aws_sdk_iot_jobs_data_plane.types.queued_at
    import aws_sdk_iot_jobs_data_plane.types.started_at
    import aws_sdk_iot_jobs_data_plane.types.thing_name
    import aws_sdk_iot_jobs_data_plane.types.version_number


class JobExecution(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_iot_jobs_data_plane.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    thing_name: NotRequired["aws_sdk_iot_jobs_data_plane.types.thing_name.ThingName"]
    """<p>The name of the thing that is executing the job.</p>"""
    status: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_execution_status.JobExecutionStatus"
    ]
    r"""<p>The status of the job execution. Can be one of: \"QUEUED\", \"IN_PROGRESS\", \"FAILED\", \"SUCCESS\", \"CANCELED\", \"TIMED_OUT\", \"REJECTED\", or \"REMOVED\".</p>"""
    status_details: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.details_map.DetailsMap"
    ]
    """<p>A collection of name/value pairs that describe the status of the job execution.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>"""
    queued_at: "aws_sdk_iot_jobs_data_plane.types.queued_at.QueuedAt"
    """<p>The time, in seconds since the epoch, when the job execution was enqueued.</p>"""
    started_at: NotRequired["aws_sdk_iot_jobs_data_plane.types.started_at.StartedAt"]
    """<p>The time, in seconds since the epoch, when the job execution was started.</p>"""
    last_updated_at: "aws_sdk_iot_jobs_data_plane.types.last_updated_at.LastUpdatedAt"
    """<p>The time, in seconds since the epoch, when the job execution was last updated. </p>"""
    approximate_seconds_before_timed_out: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.approximate_seconds_before_timed_out.ApproximateSecondsBeforeTimedOut"
    ]
    """<p>The estimated number of seconds that remain before the job execution status will be changed to <code>TIMED_OUT</code>. The actual job execution timeout can occur up to 60 seconds later than the estimated duration.</p>"""
    version_number: "aws_sdk_iot_jobs_data_plane.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time they are updated by a device.</p>"""
    execution_number: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
    ]
    """<p>A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.</p>"""
    job_document: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_document.JobDocument"
    ]
    """<p>The content of the job document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecution) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "status" in value:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_status

        out["status"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_status.serialize_json(
                value["status"]
            )
        )
    if "status_details" in value:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["statusDetails"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.serialize_json(
                value["status_details"]
            )
        )
    out["queuedAt"] = value.get("queued_at", 0)
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    out["lastUpdatedAt"] = value.get("last_updated_at", 0)
    if "approximate_seconds_before_timed_out" in value:
        out["approximateSecondsBeforeTimedOut"] = value[
            "approximate_seconds_before_timed_out"
        ]
    out["versionNumber"] = value.get("version_number", 0)
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    if "job_document" in value:
        out["jobDocument"] = value["job_document"]
    return out


def deserialize_json(data: dict) -> JobExecution:
    out: JobExecution = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "status" in data:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_status

        out["status"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "statusDetails" in data:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["status_details"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.deserialize_json(
                data["statusDetails"]
            )
        )
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
    if "approximateSecondsBeforeTimedOut" in data:
        out["approximate_seconds_before_timed_out"] = data[
            "approximateSecondsBeforeTimedOut"
        ]
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    if "executionNumber" in data:
        out["execution_number"] = data["executionNumber"]
    if "jobDocument" in data:
        out["job_document"] = data["jobDocument"]
    return out

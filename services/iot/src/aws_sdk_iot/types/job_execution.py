"""Generated from Smithy shape ``com.amazonaws.iot#JobExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.approximate_seconds_before_timed_out
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.execution_number
    import aws_sdk_iot.types.forced
    import aws_sdk_iot.types.job_execution_status
    import aws_sdk_iot.types.job_execution_status_details
    import aws_sdk_iot.types.job_id
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.version_number


class JobExecution(TypedDict):
    job_id: NotRequired["aws_sdk_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to the job when it was created.</p>"""
    status: NotRequired["aws_sdk_iot.types.job_execution_status.JobExecutionStatus"]
    """<p>The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT, CANCELED, or REJECTED).</p>"""
    force_canceled: NotRequired["aws_sdk_iot.types.forced.Forced"]
    """<p>Will be <code>true</code> if the job execution was canceled with the optional <code>force</code> parameter set to <code>true</code>.</p>"""
    status_details: NotRequired[
        "aws_sdk_iot.types.job_execution_status_details.JobExecutionStatusDetails"
    ]
    """<p>A collection of name/value pairs that describe the status of the job execution.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing on which the job execution is running.</p>"""
    queued_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was queued.</p>"""
    started_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution started.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was last updated.</p>"""
    execution_number: NotRequired["aws_sdk_iot.types.execution_number.ExecutionNumber"]
    """<p>A string (consisting of the digits \"0\" through \"9\") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information. </p>"""
    version_number: "aws_sdk_iot.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time they are updated by a device.</p>"""
    approximate_seconds_before_timed_out: NotRequired[
        "aws_sdk_iot.types.approximate_seconds_before_timed_out.ApproximateSecondsBeforeTimedOut"
    ]
    """<p>The estimated number of seconds that remain before the job execution status will be changed to <code>TIMED_OUT</code>. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the estimated duration. This value will not be included if the job execution has reached a terminal status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecution) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "status" in value:
        import aws_sdk_iot.types.job_execution_status

        out["status"] = aws_sdk_iot.types.job_execution_status.serialize_json(
            value["status"]
        )
    if "force_canceled" in value:
        out["forceCanceled"] = value["force_canceled"]
    if "status_details" in value:
        import aws_sdk_iot.types.job_execution_status_details

        out["statusDetails"] = (
            aws_sdk_iot.types.job_execution_status_details.serialize_json(
                value["status_details"]
            )
        )
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "queued_at" in value:
        import aws_sdk_iot.types.date_type

        out["queuedAt"] = aws_sdk_iot.types.date_type.serialize_json(value["queued_at"])
    if "started_at" in value:
        import aws_sdk_iot.types.date_type

        out["startedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["started_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    out["versionNumber"] = value.get("version_number", 0)
    if "approximate_seconds_before_timed_out" in value:
        out["approximateSecondsBeforeTimedOut"] = value[
            "approximate_seconds_before_timed_out"
        ]
    return out


def deserialize_json(data: dict) -> JobExecution:
    out: JobExecution = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "status" in data:
        import aws_sdk_iot.types.job_execution_status

        out["status"] = aws_sdk_iot.types.job_execution_status.deserialize_json(
            data["status"]
        )
    if "forceCanceled" in data:
        out["force_canceled"] = data["forceCanceled"]
    if "statusDetails" in data:
        import aws_sdk_iot.types.job_execution_status_details

        out["status_details"] = (
            aws_sdk_iot.types.job_execution_status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "queuedAt" in data:
        import aws_sdk_iot.types.date_type

        out["queued_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["queuedAt"]
        )
    if "startedAt" in data:
        import aws_sdk_iot.types.date_type

        out["started_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["startedAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "executionNumber" in data:
        out["execution_number"] = data["executionNumber"]
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    if "approximateSecondsBeforeTimedOut" in data:
        out["approximate_seconds_before_timed_out"] = data[
            "approximateSecondsBeforeTimedOut"
        ]
    return out

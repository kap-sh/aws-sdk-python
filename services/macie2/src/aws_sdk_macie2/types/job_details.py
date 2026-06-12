"""Generated from Smithy shape ``com.amazonaws.macie2#JobDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.is_defined_in_job
    import aws_sdk_macie2.types.is_monitored_by_job


class JobDetails(TypedDict):
    is_defined_in_job: NotRequired[
        "aws_sdk_macie2.types.is_defined_in_job.IsDefinedInJob"
    ]
    """<p>Specifies whether any one-time or recurring jobs are configured to analyze objects in the bucket. Possible values are:</p> <ul><li><p>TRUE - The bucket is explicitly included in the bucket definition (S3BucketDefinitionForJob) for one or more jobs and at least one of those jobs has a status other than CANCELLED. Or the bucket matched the bucket criteria (S3BucketCriteriaForJob) for at least one job that previously ran.</p></li> <li><p>FALSE - The bucket isn't explicitly included in the bucket definition (S3BucketDefinitionForJob) for any jobs, all the jobs that explicitly include the bucket in their bucket definitions have a status of CANCELLED, or the bucket didn't match the bucket criteria (S3BucketCriteriaForJob) for any jobs that previously ran.</p></li> <li><p>UNKNOWN - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.</p></li></ul>"""
    is_monitored_by_job: NotRequired[
        "aws_sdk_macie2.types.is_monitored_by_job.IsMonitoredByJob"
    ]
    """<p>Specifies whether any recurring jobs are configured to analyze objects in the bucket. Possible values are:</p> <ul><li><p>TRUE - The bucket is explicitly included in the bucket definition (S3BucketDefinitionForJob) for one or more recurring jobs or the bucket matches the bucket criteria (S3BucketCriteriaForJob) for one or more recurring jobs. At least one of those jobs has a status other than CANCELLED.</p></li> <li><p>FALSE - The bucket isn't explicitly included in the bucket definition (S3BucketDefinitionForJob) for any recurring jobs, the bucket doesn't match the bucket criteria (S3BucketCriteriaForJob) for any recurring jobs, or all the recurring jobs that are configured to analyze data in the bucket have a status of CANCELLED.</p></li> <li><p>UNKNOWN - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.</p></li></ul>"""
    last_job_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the job that ran most recently and is configured to analyze objects in the bucket, either the latest run of a recurring job or the only run of a one-time job.</p> <p>This value is typically null if the value for the isDefinedInJob property is FALSE or UNKNOWN.</p>"""
    last_job_run_time: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job (lastJobId) started. If the job is a recurring job, this value indicates when the most recent run started.</p> <p>This value is typically null if the value for the isDefinedInJob property is FALSE or UNKNOWN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetails) -> dict:
    out: dict = {}
    if "is_defined_in_job" in value:
        import aws_sdk_macie2.types.is_defined_in_job

        out["isDefinedInJob"] = aws_sdk_macie2.types.is_defined_in_job.serialize_json(
            value["is_defined_in_job"]
        )
    if "is_monitored_by_job" in value:
        import aws_sdk_macie2.types.is_monitored_by_job

        out["isMonitoredByJob"] = (
            aws_sdk_macie2.types.is_monitored_by_job.serialize_json(
                value["is_monitored_by_job"]
            )
        )
    if "last_job_id" in value:
        out["lastJobId"] = value["last_job_id"]
    if "last_job_run_time" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["lastJobRunTime"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_job_run_time"]
        )
    return out


def deserialize_json(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if "isDefinedInJob" in data:
        import aws_sdk_macie2.types.is_defined_in_job

        out["is_defined_in_job"] = (
            aws_sdk_macie2.types.is_defined_in_job.deserialize_json(
                data["isDefinedInJob"]
            )
        )
    if "isMonitoredByJob" in data:
        import aws_sdk_macie2.types.is_monitored_by_job

        out["is_monitored_by_job"] = (
            aws_sdk_macie2.types.is_monitored_by_job.deserialize_json(
                data["isMonitoredByJob"]
            )
        )
    if "lastJobId" in data:
        out["last_job_id"] = data["lastJobId"]
    if "lastJobRunTime" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["last_job_run_time"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["lastJobRunTime"]
            )
        )
    return out

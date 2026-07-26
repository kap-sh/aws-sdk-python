"""Generated from Smithy shape ``com.amazonaws.macie2#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_s3_bucket_definition_for_job
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601
    import capo_macie2.types.job_status
    import capo_macie2.types.job_type
    import capo_macie2.types.last_run_error_status
    import capo_macie2.types.s3_bucket_criteria_for_job
    import capo_macie2.types.user_paused_details


class JobSummary(TypedDict, closed=True):
    bucket_criteria: NotRequired[
        "capo_macie2.types.s3_bucket_criteria_for_job.S3BucketCriteriaForJob"
    ]
    """<p>The property- and tag-based conditions that determine which S3 buckets are included or excluded from the job's analysis. Each time the job runs, the job uses these criteria to determine which buckets to analyze. A job's definition can contain a bucketCriteria object or a bucketDefinitions array, not both.</p>"""
    bucket_definitions: NotRequired[
        "capo_macie2.types.__list_of_s3_bucket_definition_for_job.__listOfS3BucketDefinitionForJob"
    ]
    """<p>An array of objects, one for each Amazon Web Services account that owns specific S3 buckets for the job to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A job's definition can contain a bucketDefinitions array or a bucketCriteria object, not both.</p>"""
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job was created.</p>"""
    job_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the job.</p>"""
    job_status: NotRequired["capo_macie2.types.job_status.JobStatus"]
    """<p>The current status of the job. Possible values are:</p> <ul><li><p>CANCELLED - You cancelled the job or, if it's a one-time job, you paused the job and didn't resume it within 30 days.</p></li> <li><p>COMPLETE - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesn't apply to recurring jobs.</p></li> <li><p>IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn't apply to one-time jobs.</p></li> <li><p>PAUSED - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for.</p></li> <li><p>RUNNING - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress.</p></li> <li><p>USER_PAUSED - You paused the job. If you paused the job while it had a status of RUNNING and you don't resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the job's type. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.</p></li></ul>"""
    job_type: NotRequired["capo_macie2.types.job_type.JobType"]
    """<p>The schedule for running the job. Possible values are:</p> <ul><li><p>ONE_TIME - The job runs only once.</p></li> <li><p>SCHEDULED - The job runs on a daily, weekly, or monthly basis.</p></li></ul>"""
    last_run_error_status: NotRequired[
        "capo_macie2.types.last_run_error_status.LastRunErrorStatus"
    ]
    """<p>Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom name of the job.</p>"""
    user_paused_details: NotRequired[
        "capo_macie2.types.user_paused_details.UserPausedDetails"
    ]
    """<p>If the current status of the job is USER_PAUSED, specifies when the job was paused and when the job or job run will expire and be cancelled if it isn't resumed. This value is present only if the value for jobStatus is USER_PAUSED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    if "bucket_criteria" in value:
        import capo_macie2.types.s3_bucket_criteria_for_job

        out["bucketCriteria"] = (
            capo_macie2.types.s3_bucket_criteria_for_job.serialize_json(
                value["bucket_criteria"]
            )
        )
    if "bucket_definitions" in value:
        import capo_macie2.types.__list_of_s3_bucket_definition_for_job

        out["bucketDefinitions"] = (
            capo_macie2.types.__list_of_s3_bucket_definition_for_job.serialize_json(
                value["bucket_definitions"]
            )
        )
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_status" in value:
        import capo_macie2.types.job_status

        out["jobStatus"] = capo_macie2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "job_type" in value:
        import capo_macie2.types.job_type

        out["jobType"] = capo_macie2.types.job_type.serialize_json(value["job_type"])
    if "last_run_error_status" in value:
        import capo_macie2.types.last_run_error_status

        out["lastRunErrorStatus"] = (
            capo_macie2.types.last_run_error_status.serialize_json(
                value["last_run_error_status"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "user_paused_details" in value:
        import capo_macie2.types.user_paused_details

        out["userPausedDetails"] = capo_macie2.types.user_paused_details.serialize_json(
            value["user_paused_details"]
        )
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "bucketCriteria" in data:
        import capo_macie2.types.s3_bucket_criteria_for_job

        out["bucket_criteria"] = (
            capo_macie2.types.s3_bucket_criteria_for_job.deserialize_json(
                data["bucketCriteria"]
            )
        )
    if "bucketDefinitions" in data:
        import capo_macie2.types.__list_of_s3_bucket_definition_for_job

        out["bucket_definitions"] = (
            capo_macie2.types.__list_of_s3_bucket_definition_for_job.deserialize_json(
                data["bucketDefinitions"]
            )
        )
    if "createdAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobStatus" in data:
        import capo_macie2.types.job_status

        out["job_status"] = capo_macie2.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    if "jobType" in data:
        import capo_macie2.types.job_type

        out["job_type"] = capo_macie2.types.job_type.deserialize_json(data["jobType"])
    if "lastRunErrorStatus" in data:
        import capo_macie2.types.last_run_error_status

        out["last_run_error_status"] = (
            capo_macie2.types.last_run_error_status.deserialize_json(
                data["lastRunErrorStatus"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "userPausedDetails" in data:
        import capo_macie2.types.user_paused_details

        out["user_paused_details"] = (
            capo_macie2.types.user_paused_details.deserialize_json(
                data["userPausedDetails"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeClassificationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.job_schedule_frequency
    import aws_sdk_macie2.types.job_status
    import aws_sdk_macie2.types.job_type
    import aws_sdk_macie2.types.last_run_error_status
    import aws_sdk_macie2.types.managed_data_identifier_selector
    import aws_sdk_macie2.types.s3_job_definition
    import aws_sdk_macie2.types.statistics
    import aws_sdk_macie2.types.tag_map
    import aws_sdk_macie2.types.user_paused_details


class DescribeClassificationJobResponse(TypedDict):
    allow_list_ids: NotRequired[
        "aws_sdk_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each allow list that the job is configured to use when it analyzes data.</p>"""
    client_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The token that was provided to ensure the idempotency of the request to create the job.</p>"""
    created_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job was created.</p>"""
    custom_data_identifier_ids: NotRequired[
        "aws_sdk_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each custom data identifier that the job is configured to use when it analyzes data. This value is null if the job is configured to use only managed data identifiers to analyze data.</p>"""
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom description of the job.</p>"""
    initial_run: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>For a recurring job, specifies whether you configured the job to analyze all existing, eligible objects immediately after the job was created (true). If you configured the job to analyze only those objects that were created or changed after the job was created and before the job's first scheduled run, this value is false. This value is also false for a one-time job.</p>"""
    job_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the job.</p>"""
    job_status: NotRequired["aws_sdk_macie2.types.job_status.JobStatus"]
    """<p>The current status of the job. Possible values are:</p> <ul><li><p>CANCELLED - You cancelled the job or, if it's a one-time job, you paused the job and didn't resume it within 30 days.</p></li> <li><p>COMPLETE - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesn't apply to recurring jobs.</p></li> <li><p>IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn't apply to one-time jobs.</p></li> <li><p>PAUSED - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for.</p></li> <li><p>RUNNING - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress.</p></li> <li><p>USER_PAUSED - You paused the job. If you paused the job while it had a status of RUNNING and you don't resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the job's type. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.</p></li></ul>"""
    job_type: NotRequired["aws_sdk_macie2.types.job_type.JobType"]
    """<p>The schedule for running the job. Possible values are:</p> <ul><li><p>ONE_TIME - The job runs only once.</p></li> <li><p>SCHEDULED - The job runs on a daily, weekly, or monthly basis. The scheduleFrequency property indicates the recurrence pattern for the job.</p></li></ul>"""
    last_run_error_status: NotRequired[
        "aws_sdk_macie2.types.last_run_error_status.LastRunErrorStatus"
    ]
    """<p>Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run.</p>"""
    last_run_time: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job started. If the job is a recurring job, this value indicates when the most recent run started or, if the job hasn't run yet, when the job was created.</p>"""
    managed_data_identifier_ids: NotRequired[
        "aws_sdk_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each managed data identifier that the job is explicitly configured to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type specified for the job (managedDataIdentifierSelector).</p><p>This value is null if the job's managed data identifier selection type is ALL, NONE, or RECOMMENDED.</p>"""
    managed_data_identifier_selector: NotRequired[
        "aws_sdk_macie2.types.managed_data_identifier_selector.ManagedDataIdentifierSelector"
    ]
    r"""<p>The selection type that determines which managed data identifiers the job uses when it analyzes data. Possible values are:</p> <ul><li><p>ALL - Use all managed data identifiers.</p></li> <li><p>EXCLUDE - Use all managed data identifiers except the ones specified by the managedDataIdentifierIds property.</p></li> <li><p>INCLUDE - Use only the managed data identifiers specified by the managedDataIdentifierIds property.</p></li> <li><p>NONE - Don't use any managed data identifiers. Use only custom data identifiers (customDataIdentifierIds).</p></li> <li><p>RECOMMENDED (default) - Use the recommended set of managed data identifiers.</p></li></ul> <p>If this value is null, the job uses the recommended set of managed data identifiers.</p> <p>If the job is a recurring job and this value is ALL or EXCLUDE, each job run automatically uses new managed data identifiers that are released. If this value is null or RECOMMENDED for a recurring job, each job run uses all the managed data identifiers that are in the recommended set when the run starts.</p> <p>To learn about individual managed data identifiers or determine which ones are in the recommended set, see <a href=\"https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html\">Using managed data identifiers</a> or <a href=\"https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html\">Recommended managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom name of the job.</p>"""
    s3_job_definition: NotRequired[
        "aws_sdk_macie2.types.s3_job_definition.S3JobDefinition"
    ]
    """<p>The S3 buckets that contain the objects to analyze, and the scope of that analysis.</p>"""
    sampling_percentage: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The sampling depth, as a percentage, that determines the percentage of eligible objects that the job analyzes.</p>"""
    schedule_frequency: NotRequired[
        "aws_sdk_macie2.types.job_schedule_frequency.JobScheduleFrequency"
    ]
    """<p>The recurrence pattern for running the job. This value is null if the job is configured to run only once.</p>"""
    statistics: NotRequired["aws_sdk_macie2.types.statistics.Statistics"]
    """<p>The number of times that the job has run and processing statistics for the job's current run.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the job.</p>"""
    user_paused_details: NotRequired[
        "aws_sdk_macie2.types.user_paused_details.UserPausedDetails"
    ]
    """<p>If the current status of the job is USER_PAUSED, specifies when the job was paused and when the job or job run will expire and be cancelled if it isn't resumed. This value is present only if the value for jobStatus is USER_PAUSED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClassificationJobResponse) -> dict:
    out: dict = {}
    if "allow_list_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["allowListIds"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["allow_list_ids"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "created_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "custom_data_identifier_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["customDataIdentifierIds"] = (
            aws_sdk_macie2.types.__list_of__string.serialize_json(
                value["custom_data_identifier_ids"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "initial_run" in value:
        out["initialRun"] = value["initial_run"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_status" in value:
        import aws_sdk_macie2.types.job_status

        out["jobStatus"] = aws_sdk_macie2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "job_type" in value:
        import aws_sdk_macie2.types.job_type

        out["jobType"] = aws_sdk_macie2.types.job_type.serialize_json(value["job_type"])
    if "last_run_error_status" in value:
        import aws_sdk_macie2.types.last_run_error_status

        out["lastRunErrorStatus"] = (
            aws_sdk_macie2.types.last_run_error_status.serialize_json(
                value["last_run_error_status"]
            )
        )
    if "last_run_time" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["lastRunTime"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_run_time"]
        )
    if "managed_data_identifier_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["managedDataIdentifierIds"] = (
            aws_sdk_macie2.types.__list_of__string.serialize_json(
                value["managed_data_identifier_ids"]
            )
        )
    if "managed_data_identifier_selector" in value:
        import aws_sdk_macie2.types.managed_data_identifier_selector

        out["managedDataIdentifierSelector"] = (
            aws_sdk_macie2.types.managed_data_identifier_selector.serialize_json(
                value["managed_data_identifier_selector"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "s3_job_definition" in value:
        import aws_sdk_macie2.types.s3_job_definition

        out["s3JobDefinition"] = aws_sdk_macie2.types.s3_job_definition.serialize_json(
            value["s3_job_definition"]
        )
    if "sampling_percentage" in value:
        out["samplingPercentage"] = value["sampling_percentage"]
    if "schedule_frequency" in value:
        import aws_sdk_macie2.types.job_schedule_frequency

        out["scheduleFrequency"] = (
            aws_sdk_macie2.types.job_schedule_frequency.serialize_json(
                value["schedule_frequency"]
            )
        )
    if "statistics" in value:
        import aws_sdk_macie2.types.statistics

        out["statistics"] = aws_sdk_macie2.types.statistics.serialize_json(
            value["statistics"]
        )
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    if "user_paused_details" in value:
        import aws_sdk_macie2.types.user_paused_details

        out["userPausedDetails"] = (
            aws_sdk_macie2.types.user_paused_details.serialize_json(
                value["user_paused_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClassificationJobResponse:
    out: DescribeClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if "allowListIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["allow_list_ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["allowListIds"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "createdAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["created_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "customDataIdentifierIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["custom_data_identifier_ids"] = (
            aws_sdk_macie2.types.__list_of__string.deserialize_json(
                data["customDataIdentifierIds"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "initialRun" in data:
        out["initial_run"] = data["initialRun"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobStatus" in data:
        import aws_sdk_macie2.types.job_status

        out["job_status"] = aws_sdk_macie2.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    if "jobType" in data:
        import aws_sdk_macie2.types.job_type

        out["job_type"] = aws_sdk_macie2.types.job_type.deserialize_json(
            data["jobType"]
        )
    if "lastRunErrorStatus" in data:
        import aws_sdk_macie2.types.last_run_error_status

        out["last_run_error_status"] = (
            aws_sdk_macie2.types.last_run_error_status.deserialize_json(
                data["lastRunErrorStatus"]
            )
        )
    if "lastRunTime" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["last_run_time"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["lastRunTime"]
            )
        )
    if "managedDataIdentifierIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["managed_data_identifier_ids"] = (
            aws_sdk_macie2.types.__list_of__string.deserialize_json(
                data["managedDataIdentifierIds"]
            )
        )
    if "managedDataIdentifierSelector" in data:
        import aws_sdk_macie2.types.managed_data_identifier_selector

        out["managed_data_identifier_selector"] = (
            aws_sdk_macie2.types.managed_data_identifier_selector.deserialize_json(
                data["managedDataIdentifierSelector"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "s3JobDefinition" in data:
        import aws_sdk_macie2.types.s3_job_definition

        out["s3_job_definition"] = (
            aws_sdk_macie2.types.s3_job_definition.deserialize_json(
                data["s3JobDefinition"]
            )
        )
    if "samplingPercentage" in data:
        out["sampling_percentage"] = data["samplingPercentage"]
    if "scheduleFrequency" in data:
        import aws_sdk_macie2.types.job_schedule_frequency

        out["schedule_frequency"] = (
            aws_sdk_macie2.types.job_schedule_frequency.deserialize_json(
                data["scheduleFrequency"]
            )
        )
    if "statistics" in data:
        import aws_sdk_macie2.types.statistics

        out["statistics"] = aws_sdk_macie2.types.statistics.deserialize_json(
            data["statistics"]
        )
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    if "userPausedDetails" in data:
        import aws_sdk_macie2.types.user_paused_details

        out["user_paused_details"] = (
            aws_sdk_macie2.types.user_paused_details.deserialize_json(
                data["userPausedDetails"]
            )
        )
    return out

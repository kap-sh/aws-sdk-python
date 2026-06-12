"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Job``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__integer_min_negative50_max50
    import aws_sdk_mediaconvert.types.__list_of_hop_destination
    import aws_sdk_mediaconvert.types.__list_of_output_group_detail
    import aws_sdk_mediaconvert.types.__list_of_queue_transition
    import aws_sdk_mediaconvert.types.__list_of_warning_group
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__timestamp_unix
    import aws_sdk_mediaconvert.types.acceleration_settings
    import aws_sdk_mediaconvert.types.acceleration_status
    import aws_sdk_mediaconvert.types.billing_tags_source
    import aws_sdk_mediaconvert.types.elemental_inference_configuration
    import aws_sdk_mediaconvert.types.job_messages
    import aws_sdk_mediaconvert.types.job_phase
    import aws_sdk_mediaconvert.types.job_settings
    import aws_sdk_mediaconvert.types.job_status
    import aws_sdk_mediaconvert.types.share_status
    import aws_sdk_mediaconvert.types.simulate_reserved_queue
    import aws_sdk_mediaconvert.types.status_update_interval
    import aws_sdk_mediaconvert.types.timing


class Job(TypedDict):
    acceleration_settings: NotRequired[
        "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Accelerated transcoding can significantly speed up jobs with long, visually complex content."""
    acceleration_status: NotRequired[
        "aws_sdk_mediaconvert.types.acceleration_status.AccelerationStatus"
    ]
    """Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings aren't compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT_ACCELERATED."""
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    billing_tags_source: NotRequired[
        "aws_sdk_mediaconvert.types.billing_tags_source.BillingTagsSource"
    ]
    """The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up."""
    client_request_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html."""
    created_at: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The time, in Unix epoch format in seconds, when the job got created."""
    current_phase: NotRequired["aws_sdk_mediaconvert.types.job_phase.JobPhase"]
    """A job's phase can be PROBING, TRANSCODING OR UPLOADING"""
    elemental_inference_configuration: NotRequired[
        "aws_sdk_mediaconvert.types.elemental_inference_configuration.ElementalInferenceConfiguration"
    ]
    """The Elemental Inference configuration used in this job."""
    error_code: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Error code for the job"""
    error_message: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Error message of Job"""
    hop_destinations: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional list of hop destinations."""
    id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """A portion of the job's ARN, unique within your AWS Elemental MediaConvert resources"""
    job_engine_version_requested: NotRequired[
        "aws_sdk_mediaconvert.types.__string.__string"
    ]
    """The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format."""
    job_engine_version_used: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The Job engine version that your job used. Job engine versions are in a YYYY-MM-DD format. When you request an expired version, the response for this property will be empty. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested. When you request an invalid version, the response for this property will be empty. Requests to create jobs with an invalid version result in a 400 error message, and no job is created."""
    job_percent_complete: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """An estimate of how far your job has progressed. This estimate is shown as a percentage of the total time from when your job leaves its queue to when your output files appear in your output Amazon S3 bucket. AWS Elemental MediaConvert provides jobPercentComplete in CloudWatch STATUS_UPDATE events and in the response to GetJob and ListJobs requests. The jobPercentComplete estimate is reliable for the following input containers: Quicktime, Transport Stream, MP4, and MXF. For some jobs, the service can't provide information about job progress. In those cases, jobPercentComplete returns a null value."""
    job_template: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The job template that the job is created from, if it is created from a job template."""
    last_share_details: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Contains information about the most recent share attempt for the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-resource-share.html"""
    messages: NotRequired["aws_sdk_mediaconvert.types.job_messages.JobMessages"]
    """Provides messages from the service about jobs that you have already successfully submitted."""
    output_group_details: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_output_group_detail.__listOfOutputGroupDetail"
    ]
    """List of output group details"""
    priority: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Relative priority on the job."""
    queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""
    queue_transitions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_queue_transition.__listOfQueueTransition"
    ]
    """The job's queue hopping history."""
    retry_count: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The number of times that the service automatically attempted to process your job after encountering an error."""
    role: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html"""
    settings: NotRequired["aws_sdk_mediaconvert.types.job_settings.JobSettings"]
    """JobSettings contains all the transcode settings for a job."""
    share_status: NotRequired["aws_sdk_mediaconvert.types.share_status.ShareStatus"]
    """A job's share status can be NOT_SHARED, INITIATED, or SHARED"""
    simulate_reserved_queue: NotRequired[
        "aws_sdk_mediaconvert.types.simulate_reserved_queue.SimulateReservedQueue"
    ]
    """Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default."""
    status: NotRequired["aws_sdk_mediaconvert.types.job_status.JobStatus"]
    """A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR."""
    status_update_interval: NotRequired[
        "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
    timing: NotRequired["aws_sdk_mediaconvert.types.timing.Timing"]
    """Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds."""
    user_metadata: NotRequired[
        "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
    ]
    """User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs."""
    warnings: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_warning_group.__listOfWarningGroup"
    ]
    """Contains any warning messages for the job. Use to help identify potential issues with your input, output, or job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "acceleration_status" in value:
        import aws_sdk_mediaconvert.types.acceleration_status

        out["accelerationStatus"] = (
            aws_sdk_mediaconvert.types.acceleration_status.serialize_json(
                value["acceleration_status"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "billing_tags_source" in value:
        import aws_sdk_mediaconvert.types.billing_tags_source

        out["billingTagsSource"] = (
            aws_sdk_mediaconvert.types.billing_tags_source.serialize_json(
                value["billing_tags_source"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "created_at" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["createdAt"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "current_phase" in value:
        import aws_sdk_mediaconvert.types.job_phase

        out["currentPhase"] = aws_sdk_mediaconvert.types.job_phase.serialize_json(
            value["current_phase"]
        )
    if "elemental_inference_configuration" in value:
        import aws_sdk_mediaconvert.types.elemental_inference_configuration

        out["elementalInferenceConfiguration"] = (
            aws_sdk_mediaconvert.types.elemental_inference_configuration.serialize_json(
                value["elemental_inference_configuration"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "hop_destinations" in value:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hopDestinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.serialize_json(
                value["hop_destinations"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "job_engine_version_requested" in value:
        out["jobEngineVersionRequested"] = value["job_engine_version_requested"]
    if "job_engine_version_used" in value:
        out["jobEngineVersionUsed"] = value["job_engine_version_used"]
    if "job_percent_complete" in value:
        out["jobPercentComplete"] = value["job_percent_complete"]
    if "job_template" in value:
        out["jobTemplate"] = value["job_template"]
    if "last_share_details" in value:
        out["lastShareDetails"] = value["last_share_details"]
    if "messages" in value:
        import aws_sdk_mediaconvert.types.job_messages

        out["messages"] = aws_sdk_mediaconvert.types.job_messages.serialize_json(
            value["messages"]
        )
    if "output_group_details" in value:
        import aws_sdk_mediaconvert.types.__list_of_output_group_detail

        out["outputGroupDetails"] = (
            aws_sdk_mediaconvert.types.__list_of_output_group_detail.serialize_json(
                value["output_group_details"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "queue_transitions" in value:
        import aws_sdk_mediaconvert.types.__list_of_queue_transition

        out["queueTransitions"] = (
            aws_sdk_mediaconvert.types.__list_of_queue_transition.serialize_json(
                value["queue_transitions"]
            )
        )
    if "retry_count" in value:
        out["retryCount"] = value["retry_count"]
    if "role" in value:
        out["role"] = value["role"]
    if "settings" in value:
        import aws_sdk_mediaconvert.types.job_settings

        out["settings"] = aws_sdk_mediaconvert.types.job_settings.serialize_json(
            value["settings"]
        )
    if "share_status" in value:
        import aws_sdk_mediaconvert.types.share_status

        out["shareStatus"] = aws_sdk_mediaconvert.types.share_status.serialize_json(
            value["share_status"]
        )
    if "simulate_reserved_queue" in value:
        import aws_sdk_mediaconvert.types.simulate_reserved_queue

        out["simulateReservedQueue"] = (
            aws_sdk_mediaconvert.types.simulate_reserved_queue.serialize_json(
                value["simulate_reserved_queue"]
            )
        )
    if "status" in value:
        import aws_sdk_mediaconvert.types.job_status

        out["status"] = aws_sdk_mediaconvert.types.job_status.serialize_json(
            value["status"]
        )
    if "status_update_interval" in value:
        import aws_sdk_mediaconvert.types.status_update_interval

        out["statusUpdateInterval"] = (
            aws_sdk_mediaconvert.types.status_update_interval.serialize_json(
                value["status_update_interval"]
            )
        )
    if "timing" in value:
        import aws_sdk_mediaconvert.types.timing

        out["timing"] = aws_sdk_mediaconvert.types.timing.serialize_json(
            value["timing"]
        )
    if "user_metadata" in value:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["userMetadata"] = (
            aws_sdk_mediaconvert.types.__map_of__string.serialize_json(
                value["user_metadata"]
            )
        )
    if "warnings" in value:
        import aws_sdk_mediaconvert.types.__list_of_warning_group

        out["warnings"] = (
            aws_sdk_mediaconvert.types.__list_of_warning_group.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "accelerationSettings" in data:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if "accelerationStatus" in data:
        import aws_sdk_mediaconvert.types.acceleration_status

        out["acceleration_status"] = (
            aws_sdk_mediaconvert.types.acceleration_status.deserialize_json(
                data["accelerationStatus"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "billingTagsSource" in data:
        import aws_sdk_mediaconvert.types.billing_tags_source

        out["billing_tags_source"] = (
            aws_sdk_mediaconvert.types.billing_tags_source.deserialize_json(
                data["billingTagsSource"]
            )
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "createdAt" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["created_at"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["createdAt"]
            )
        )
    if "currentPhase" in data:
        import aws_sdk_mediaconvert.types.job_phase

        out["current_phase"] = aws_sdk_mediaconvert.types.job_phase.deserialize_json(
            data["currentPhase"]
        )
    if "elementalInferenceConfiguration" in data:
        import aws_sdk_mediaconvert.types.elemental_inference_configuration

        out["elemental_inference_configuration"] = (
            aws_sdk_mediaconvert.types.elemental_inference_configuration.deserialize_json(
                data["elementalInferenceConfiguration"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "hopDestinations" in data:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hop_destinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.deserialize_json(
                data["hopDestinations"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "jobEngineVersionRequested" in data:
        out["job_engine_version_requested"] = data["jobEngineVersionRequested"]
    if "jobEngineVersionUsed" in data:
        out["job_engine_version_used"] = data["jobEngineVersionUsed"]
    if "jobPercentComplete" in data:
        out["job_percent_complete"] = data["jobPercentComplete"]
    if "jobTemplate" in data:
        out["job_template"] = data["jobTemplate"]
    if "lastShareDetails" in data:
        out["last_share_details"] = data["lastShareDetails"]
    if "messages" in data:
        import aws_sdk_mediaconvert.types.job_messages

        out["messages"] = aws_sdk_mediaconvert.types.job_messages.deserialize_json(
            data["messages"]
        )
    if "outputGroupDetails" in data:
        import aws_sdk_mediaconvert.types.__list_of_output_group_detail

        out["output_group_details"] = (
            aws_sdk_mediaconvert.types.__list_of_output_group_detail.deserialize_json(
                data["outputGroupDetails"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "queue" in data:
        out["queue"] = data["queue"]
    if "queueTransitions" in data:
        import aws_sdk_mediaconvert.types.__list_of_queue_transition

        out["queue_transitions"] = (
            aws_sdk_mediaconvert.types.__list_of_queue_transition.deserialize_json(
                data["queueTransitions"]
            )
        )
    if "retryCount" in data:
        out["retry_count"] = data["retryCount"]
    if "role" in data:
        out["role"] = data["role"]
    if "settings" in data:
        import aws_sdk_mediaconvert.types.job_settings

        out["settings"] = aws_sdk_mediaconvert.types.job_settings.deserialize_json(
            data["settings"]
        )
    if "shareStatus" in data:
        import aws_sdk_mediaconvert.types.share_status

        out["share_status"] = aws_sdk_mediaconvert.types.share_status.deserialize_json(
            data["shareStatus"]
        )
    if "simulateReservedQueue" in data:
        import aws_sdk_mediaconvert.types.simulate_reserved_queue

        out["simulate_reserved_queue"] = (
            aws_sdk_mediaconvert.types.simulate_reserved_queue.deserialize_json(
                data["simulateReservedQueue"]
            )
        )
    if "status" in data:
        import aws_sdk_mediaconvert.types.job_status

        out["status"] = aws_sdk_mediaconvert.types.job_status.deserialize_json(
            data["status"]
        )
    if "statusUpdateInterval" in data:
        import aws_sdk_mediaconvert.types.status_update_interval

        out["status_update_interval"] = (
            aws_sdk_mediaconvert.types.status_update_interval.deserialize_json(
                data["statusUpdateInterval"]
            )
        )
    if "timing" in data:
        import aws_sdk_mediaconvert.types.timing

        out["timing"] = aws_sdk_mediaconvert.types.timing.deserialize_json(
            data["timing"]
        )
    if "userMetadata" in data:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["user_metadata"] = (
            aws_sdk_mediaconvert.types.__map_of__string.deserialize_json(
                data["userMetadata"]
            )
        )
    if "warnings" in data:
        import aws_sdk_mediaconvert.types.__list_of_warning_group

        out["warnings"] = (
            aws_sdk_mediaconvert.types.__list_of_warning_group.deserialize_json(
                data["warnings"]
            )
        )
    return out

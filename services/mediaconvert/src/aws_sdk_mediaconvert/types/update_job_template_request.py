"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UpdateJobTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min_negative50_max50
    import aws_sdk_mediaconvert.types.__list_of_hop_destination
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.acceleration_settings
    import aws_sdk_mediaconvert.types.job_template_settings
    import aws_sdk_mediaconvert.types.status_update_interval


class UpdateJobTemplateRequest(TypedDict):
    acceleration_settings: NotRequired[
        "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide."""
    category: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The new category for the job template, if you are changing it."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The new description for the job template, if you are changing it."""
    hop_destinations: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional list of hop destinations."""
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the job template you are modifying"""
    priority: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0."""
    queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The new queue for the job template, if you are changing it."""
    settings: NotRequired[
        "aws_sdk_mediaconvert.types.job_template_settings.JobTemplateSettings"
    ]
    """JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it."""
    status_update_interval: NotRequired[
        "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobTemplateRequest) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "category" in value:
        out["category"] = value["category"]
    if "description" in value:
        out["description"] = value["description"]
    if "hop_destinations" in value:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hopDestinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.serialize_json(
                value["hop_destinations"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "settings" in value:
        import aws_sdk_mediaconvert.types.job_template_settings

        out["settings"] = (
            aws_sdk_mediaconvert.types.job_template_settings.serialize_json(
                value["settings"]
            )
        )
    if "status_update_interval" in value:
        import aws_sdk_mediaconvert.types.status_update_interval

        out["statusUpdateInterval"] = (
            aws_sdk_mediaconvert.types.status_update_interval.serialize_json(
                value["status_update_interval"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJobTemplateRequest:
    out: UpdateJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if "accelerationSettings" in data:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if "category" in data:
        out["category"] = data["category"]
    if "description" in data:
        out["description"] = data["description"]
    if "hopDestinations" in data:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hop_destinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.deserialize_json(
                data["hopDestinations"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "queue" in data:
        out["queue"] = data["queue"]
    if "settings" in data:
        import aws_sdk_mediaconvert.types.job_template_settings

        out["settings"] = (
            aws_sdk_mediaconvert.types.job_template_settings.deserialize_json(
                data["settings"]
            )
        )
    if "statusUpdateInterval" in data:
        import aws_sdk_mediaconvert.types.status_update_interval

        out["status_update_interval"] = (
            aws_sdk_mediaconvert.types.status_update_interval.deserialize_json(
                data["statusUpdateInterval"]
            )
        )
    return out

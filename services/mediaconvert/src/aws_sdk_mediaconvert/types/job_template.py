"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min_negative50_max50
    import aws_sdk_mediaconvert.types.__list_of_hop_destination
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__timestamp_unix
    import aws_sdk_mediaconvert.types.acceleration_settings
    import aws_sdk_mediaconvert.types.job_template_settings
    import aws_sdk_mediaconvert.types.status_update_interval
    import aws_sdk_mediaconvert.types.type


class JobTemplate(TypedDict):
    acceleration_settings: NotRequired[
        "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Accelerated transcoding can significantly speed up jobs with long, visually complex content."""
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    category: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An optional category you create to organize your job templates."""
    created_at: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds for Job template creation."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An optional description you create for each job template."""
    hop_destinations: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional list of hop destinations."""
    last_updated: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds when the Job template was last updated."""
    name: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """A name you create for each job template. Each name must be unique within your account."""
    priority: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Relative priority on the job."""
    queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. The queue that jobs created from this template are assigned to. If you don't specify this, jobs will go to the default queue."""
    settings: NotRequired[
        "aws_sdk_mediaconvert.types.job_template_settings.JobTemplateSettings"
    ]
    """JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it."""
    status_update_interval: NotRequired[
        "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
    type: NotRequired["aws_sdk_mediaconvert.types.type.Type"]
    """A job template can be of two types: system or custom. System or built-in job templates can't be modified or deleted by the user."""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplate) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "category" in value:
        out["category"] = value["category"]
    if "created_at" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["createdAt"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "hop_destinations" in value:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hopDestinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.serialize_json(
                value["hop_destinations"]
            )
        )
    if "last_updated" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["lastUpdated"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["last_updated"]
        )
    if "name" in value:
        out["name"] = value["name"]
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
    if "type" in value:
        import aws_sdk_mediaconvert.types.type

        out["type"] = aws_sdk_mediaconvert.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> JobTemplate:
    out: JobTemplate = {}  # type: ignore[typeddict-item]
    if "accelerationSettings" in data:
        import aws_sdk_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            aws_sdk_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "category" in data:
        out["category"] = data["category"]
    if "createdAt" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["created_at"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["createdAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "hopDestinations" in data:
        import aws_sdk_mediaconvert.types.__list_of_hop_destination

        out["hop_destinations"] = (
            aws_sdk_mediaconvert.types.__list_of_hop_destination.deserialize_json(
                data["hopDestinations"]
            )
        )
    if "lastUpdated" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["last_updated"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["lastUpdated"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
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
    if "type" in data:
        import aws_sdk_mediaconvert.types.type

        out["type"] = aws_sdk_mediaconvert.types.type.deserialize_json(data["type"])
    return out

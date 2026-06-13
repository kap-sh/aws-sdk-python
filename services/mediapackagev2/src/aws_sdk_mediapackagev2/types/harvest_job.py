"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediapackagev2.types.destination
    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.harvest_job_status
    import aws_sdk_mediapackagev2.types.harvested_manifests
    import aws_sdk_mediapackagev2.types.harvester_schedule_configuration
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name


class HarvestJob(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group containing the channel associated with this harvest job.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel associated with this harvest job.</p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint associated with this harvest job.</p>"""
    destination: "aws_sdk_mediapackagev2.types.destination.Destination"
    """<p>The S3 destination where the harvested content will be placed.</p>"""
    harvest_job_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvest job.</p>"""
    harvested_manifests: (
        "aws_sdk_mediapackagev2.types.harvested_manifests.HarvestedManifests"
    )
    """<p>A list of manifests that are being or have been harvested.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description of the harvest job.</p>"""
    schedule_configuration: "aws_sdk_mediapackagev2.types.harvester_schedule_configuration.HarvesterScheduleConfiguration"
    """<p>The configuration for when the harvest job is scheduled to run.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the harvest job.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the harvest job was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the harvest job was last modified.</p>"""
    status: "aws_sdk_mediapackagev2.types.harvest_job_status.HarvestJobStatus"
    """<p>The current status of the harvest job (e.g., QUEUED, IN_PROGRESS, CANCELLED, COMPLETED, FAILED).</p>"""
    error_message: NotRequired["str"]
    """<p>An error message if the harvest job encountered any issues.</p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current version of the harvest job. Used for concurrency control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestJob) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    import aws_sdk_mediapackagev2.types.destination

    out["Destination"] = aws_sdk_mediapackagev2.types.destination.serialize_json(
        value["destination"]
    )
    out["HarvestJobName"] = value["harvest_job_name"]
    import aws_sdk_mediapackagev2.types.harvested_manifests

    out["HarvestedManifests"] = (
        aws_sdk_mediapackagev2.types.harvested_manifests.serialize_json(
            value["harvested_manifests"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_mediapackagev2.types.harvester_schedule_configuration

    out["ScheduleConfiguration"] = (
        aws_sdk_mediapackagev2.types.harvester_schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    out["Arn"] = value["arn"]
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    import aws_sdk_mediapackagev2.types.harvest_job_status

    out["Status"] = aws_sdk_mediapackagev2.types.harvest_job_status.serialize_json(
        value["status"]
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    return out


def deserialize_json(data: dict) -> HarvestJob:
    out: HarvestJob = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError("HarvestJob.channel_group_name required")
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("HarvestJob.channel_name required")
    if "OriginEndpointName" in data:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        raise DeserializationError("HarvestJob.origin_endpoint_name required")
    if "Destination" in data:
        import aws_sdk_mediapackagev2.types.destination

        out["destination"] = aws_sdk_mediapackagev2.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("HarvestJob.destination required")
    if "HarvestJobName" in data:
        out["harvest_job_name"] = data["HarvestJobName"]
    else:
        raise DeserializationError("HarvestJob.harvest_job_name required")
    if "HarvestedManifests" in data:
        import aws_sdk_mediapackagev2.types.harvested_manifests

        out["harvested_manifests"] = (
            aws_sdk_mediapackagev2.types.harvested_manifests.deserialize_json(
                data["HarvestedManifests"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.harvested_manifests required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ScheduleConfiguration" in data:
        import aws_sdk_mediapackagev2.types.harvester_schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_mediapackagev2.types.harvester_schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.schedule_configuration required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("HarvestJob.arn required")
    if "CreatedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.created_at required")
    if "ModifiedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.modified_at required")
    if "Status" in data:
        import aws_sdk_mediapackagev2.types.harvest_job_status

        out["status"] = (
            aws_sdk_mediapackagev2.types.harvest_job_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.status required")
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    return out

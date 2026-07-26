"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateHarvestJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.destination
    import capo_mediapackagev2.types.harvested_manifests
    import capo_mediapackagev2.types.harvester_schedule_configuration
    import capo_mediapackagev2.types.idempotency_token
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.tag_map


class CreateHarvestJobRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group containing the channel from which to harvest content.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel from which to harvest content.</p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint from which to harvest content.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the harvest job.</p>"""
    harvested_manifests: (
        "capo_mediapackagev2.types.harvested_manifests.HarvestedManifests"
    )
    """<p>A list of manifests to be harvested.</p>"""
    schedule_configuration: "capo_mediapackagev2.types.harvester_schedule_configuration.HarvesterScheduleConfiguration"
    """<p>The configuration for when the harvest job should run, including start and end times.</p>"""
    destination: "capo_mediapackagev2.types.destination.Destination"
    """<p>The S3 destination where the harvested content will be placed.</p>"""
    client_token: NotRequired[
        "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    harvest_job_name: NotRequired[
        "capo_mediapackagev2.types.resource_name.ResourceName"
    ]
    """<p>A name for the harvest job. This name must be unique within the channel.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    """<p>A collection of tags associated with the harvest job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarvestJobRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_mediapackagev2.types.harvested_manifests

    out["HarvestedManifests"] = (
        capo_mediapackagev2.types.harvested_manifests.serialize_json(
            value["harvested_manifests"]
        )
    )
    import capo_mediapackagev2.types.harvester_schedule_configuration

    out["ScheduleConfiguration"] = (
        capo_mediapackagev2.types.harvester_schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    import capo_mediapackagev2.types.destination

    out["Destination"] = capo_mediapackagev2.types.destination.serialize_json(
        value["destination"]
    )
    if "harvest_job_name" in value:
        out["HarvestJobName"] = value["harvest_job_name"]
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["Tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateHarvestJobRequest:
    out: CreateHarvestJobRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "HarvestedManifests" in data:
        import capo_mediapackagev2.types.harvested_manifests

        out["harvested_manifests"] = (
            capo_mediapackagev2.types.harvested_manifests.deserialize_json(
                data["HarvestedManifests"]
            )
        )
    else:
        raise DeserializationError(
            "CreateHarvestJobRequest.harvested_manifests required"
        )
    if "ScheduleConfiguration" in data:
        import capo_mediapackagev2.types.harvester_schedule_configuration

        out["schedule_configuration"] = (
            capo_mediapackagev2.types.harvester_schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateHarvestJobRequest.schedule_configuration required"
        )
    if "Destination" in data:
        import capo_mediapackagev2.types.destination

        out["destination"] = capo_mediapackagev2.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("CreateHarvestJobRequest.destination required")
    if "HarvestJobName" in data:
        out["harvest_job_name"] = data["HarvestJobName"]
    if "Tags" in data:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["Tags"])
    return out

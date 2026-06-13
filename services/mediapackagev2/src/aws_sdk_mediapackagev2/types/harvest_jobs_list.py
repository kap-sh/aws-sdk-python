"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvest_job

HarvestJobsList: TypeAlias = list["aws_sdk_mediapackagev2.types.harvest_job.HarvestJob"]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestJobsList) -> list:
    import aws_sdk_mediapackagev2.types.harvest_job

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackagev2.types.harvest_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> HarvestJobsList:
    import aws_sdk_mediapackagev2.types.harvest_job

    out: HarvestJobsList = []
    for item in data:
        out.append(aws_sdk_mediapackagev2.types.harvest_job.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfHarvestJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage.types.harvest_job

__listOfHarvestJob: TypeAlias = list["capo_mediapackage.types.harvest_job.HarvestJob"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHarvestJob) -> list:
    import capo_mediapackage.types.harvest_job

    out: list = []
    for item in value:
        out.append(capo_mediapackage.types.harvest_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHarvestJob:
    import capo_mediapackage.types.harvest_job

    out: __listOfHarvestJob = []
    for item in data:
        out.append(capo_mediapackage.types.harvest_job.deserialize_json(item))
    return out

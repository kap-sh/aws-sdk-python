"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.harvest_job

HarvestJobsList: TypeAlias = list["capo_mediapackagev2.types.harvest_job.HarvestJob"]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestJobsList) -> list:
    import capo_mediapackagev2.types.harvest_job

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.harvest_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> HarvestJobsList:
    import capo_mediapackagev2.types.harvest_job

    out: HarvestJobsList = []
    for item in data:
        out.append(capo_mediapackagev2.types.harvest_job.deserialize_json(item))
    return out

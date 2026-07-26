"""Generated from Smithy shape ``com.amazonaws.panorama#JobTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.job_resource_tags

JobTagsList: TypeAlias = list["capo_panorama.types.job_resource_tags.JobResourceTags"]


# --- restJson1 ser/de ---
def serialize_json(value: JobTagsList) -> list:
    import capo_panorama.types.job_resource_tags

    out: list = []
    for item in value:
        out.append(capo_panorama.types.job_resource_tags.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobTagsList:
    import capo_panorama.types.job_resource_tags

    out: JobTagsList = []
    for item in data:
        out.append(capo_panorama.types.job_resource_tags.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.job

__listOfJob: TypeAlias = list["capo_mediaconvert.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJob) -> list:
    import capo_mediaconvert.types.job

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJob:
    import capo_mediaconvert.types.job

    out: __listOfJob = []
    for item in data:
        out.append(capo_mediaconvert.types.job.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfJobEngineVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.job_engine_version

__listOfJobEngineVersion: TypeAlias = list[
    "capo_mediaconvert.types.job_engine_version.JobEngineVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobEngineVersion) -> list:
    import capo_mediaconvert.types.job_engine_version

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.job_engine_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobEngineVersion:
    import capo_mediaconvert.types.job_engine_version

    out: __listOfJobEngineVersion = []
    for item in data:
        out.append(capo_mediaconvert.types.job_engine_version.deserialize_json(item))
    return out

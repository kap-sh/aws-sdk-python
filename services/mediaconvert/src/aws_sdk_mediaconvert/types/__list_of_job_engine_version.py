"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfJobEngineVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.job_engine_version

__listOfJobEngineVersion: TypeAlias = list[
    "aws_sdk_mediaconvert.types.job_engine_version.JobEngineVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobEngineVersion) -> list:
    import aws_sdk_mediaconvert.types.job_engine_version

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.job_engine_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobEngineVersion:
    import aws_sdk_mediaconvert.types.job_engine_version

    out: __listOfJobEngineVersion = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.job_engine_version.deserialize_json(item))
    return out

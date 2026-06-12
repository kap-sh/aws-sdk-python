"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfJobTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.job_template

__listOfJobTemplate: TypeAlias = list[
    "aws_sdk_mediaconvert.types.job_template.JobTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobTemplate) -> list:
    import aws_sdk_mediaconvert.types.job_template

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.job_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobTemplate:
    import aws_sdk_mediaconvert.types.job_template

    out: __listOfJobTemplate = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.job_template.deserialize_json(item))
    return out

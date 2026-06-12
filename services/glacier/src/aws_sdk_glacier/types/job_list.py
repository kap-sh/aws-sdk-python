"""Generated from Smithy shape ``com.amazonaws.glacier#JobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.glacier_job_description

JobList: TypeAlias = list[
    "aws_sdk_glacier.types.glacier_job_description.GlacierJobDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobList) -> list:
    import aws_sdk_glacier.types.glacier_job_description

    out: list = []
    for item in value:
        out.append(aws_sdk_glacier.types.glacier_job_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobList:
    import aws_sdk_glacier.types.glacier_job_description

    out: JobList = []
    for item in data:
        out.append(aws_sdk_glacier.types.glacier_job_description.deserialize_json(item))
    return out

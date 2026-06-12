"""Generated from Smithy shape ``com.amazonaws.databrew#JobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job

JobList: TypeAlias = list["aws_sdk_databrew.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobList) -> list:
    import aws_sdk_databrew.types.job

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobList:
    import aws_sdk_databrew.types.job

    out: JobList = []
    for item in data:
        out.append(aws_sdk_databrew.types.job.deserialize_json(item))
    return out

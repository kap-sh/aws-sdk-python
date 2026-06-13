"""Generated from Smithy shape ``com.amazonaws.drs#JobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.job

JobsList: TypeAlias = list["aws_sdk_drs.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobsList) -> list:
    import aws_sdk_drs.types.job

    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobsList:
    import aws_sdk_drs.types.job

    out: JobsList = []
    for item in data:
        out.append(aws_sdk_drs.types.job.deserialize_json(item))
    return out

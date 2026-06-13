"""Generated from Smithy shape ``com.amazonaws.mgn#JobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job

JobsList: TypeAlias = list["aws_sdk_mgn.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobsList) -> list:
    import aws_sdk_mgn.types.job

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobsList:
    import aws_sdk_mgn.types.job

    out: JobsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.job.deserialize_json(item))
    return out

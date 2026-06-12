"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_backup.types.copy_job

CopyJobsList: TypeAlias = list["aws_sdk_backup.types.copy_job.CopyJob"]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobsList) -> list:
    import aws_sdk_backup.types.copy_job
    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.copy_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> CopyJobsList:
    import aws_sdk_backup.types.copy_job
    out: CopyJobsList = []
    for item in data:
        out.append(aws_sdk_backup.types.copy_job.deserialize_json(item))
    return out
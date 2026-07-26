"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.copy_job

CopyJobsList: TypeAlias = list["capo_backup.types.copy_job.CopyJob"]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobsList) -> list:
    import capo_backup.types.copy_job

    out: list = []
    for item in value:
        out.append(capo_backup.types.copy_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> CopyJobsList:
    import capo_backup.types.copy_job

    out: CopyJobsList = []
    for item in data:
        out.append(capo_backup.types.copy_job.deserialize_json(item))
    return out

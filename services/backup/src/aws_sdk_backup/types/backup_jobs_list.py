"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_job

BackupJobsList: TypeAlias = list["aws_sdk_backup.types.backup_job.BackupJob"]


# --- restJson1 ser/de ---
def serialize_json(value: BackupJobsList) -> list:
    import aws_sdk_backup.types.backup_job
    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.backup_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupJobsList:
    import aws_sdk_backup.types.backup_job
    out: BackupJobsList = []
    for item in data:
        out.append(aws_sdk_backup.types.backup_job.deserialize_json(item))
    return out
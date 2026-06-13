"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_job_summary

BackupJobSummaryList: TypeAlias = list[
    "aws_sdk_backup.types.backup_job_summary.BackupJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupJobSummaryList) -> list:
    import aws_sdk_backup.types.backup_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.backup_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupJobSummaryList:
    import aws_sdk_backup.types.backup_job_summary

    out: BackupJobSummaryList = []
    for item in data:
        out.append(aws_sdk_backup.types.backup_job_summary.deserialize_json(item))
    return out

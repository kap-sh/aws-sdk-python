"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_job

ScanJobs: TypeAlias = list["aws_sdk_backup.types.scan_job.ScanJob"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobs) -> list:
    import aws_sdk_backup.types.scan_job

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.scan_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanJobs:
    import aws_sdk_backup.types.scan_job

    out: ScanJobs = []
    for item in data:
        out.append(aws_sdk_backup.types.scan_job.deserialize_json(item))
    return out

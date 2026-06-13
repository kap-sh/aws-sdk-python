"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_job_summary

ScanJobSummaryList: TypeAlias = list[
    "aws_sdk_backup.types.scan_job_summary.ScanJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobSummaryList) -> list:
    import aws_sdk_backup.types.scan_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.scan_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanJobSummaryList:
    import aws_sdk_backup.types.scan_job_summary

    out: ScanJobSummaryList = []
    for item in data:
        out.append(aws_sdk_backup.types.scan_job_summary.deserialize_json(item))
    return out

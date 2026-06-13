"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.copy_job_summary

CopyJobSummaryList: TypeAlias = list[
    "aws_sdk_backup.types.copy_job_summary.CopyJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobSummaryList) -> list:
    import aws_sdk_backup.types.copy_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.copy_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CopyJobSummaryList:
    import aws_sdk_backup.types.copy_job_summary

    out: CopyJobSummaryList = []
    for item in data:
        out.append(aws_sdk_backup.types.copy_job_summary.deserialize_json(item))
    return out

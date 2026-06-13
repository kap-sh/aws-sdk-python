"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_job_summary

RestoreJobSummaryList: TypeAlias = list[
    "aws_sdk_backup.types.restore_job_summary.RestoreJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobSummaryList) -> list:
    import aws_sdk_backup.types.restore_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.restore_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RestoreJobSummaryList:
    import aws_sdk_backup.types.restore_job_summary

    out: RestoreJobSummaryList = []
    for item in data:
        out.append(aws_sdk_backup.types.restore_job_summary.deserialize_json(item))
    return out

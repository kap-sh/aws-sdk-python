"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.copy_job_summary

CopyJobSummaryList: TypeAlias = list[
    "capo_backup.types.copy_job_summary.CopyJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobSummaryList) -> list:
    import capo_backup.types.copy_job_summary

    out: list = []
    for item in value:
        out.append(capo_backup.types.copy_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CopyJobSummaryList:
    import capo_backup.types.copy_job_summary

    out: CopyJobSummaryList = []
    for item in data:
        out.append(capo_backup.types.copy_job_summary.deserialize_json(item))
    return out

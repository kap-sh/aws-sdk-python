"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.scan_job_summary

ScanJobSummaryList: TypeAlias = list[
    "capo_backup.types.scan_job_summary.ScanJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobSummaryList) -> list:
    import capo_backup.types.scan_job_summary

    out: list = []
    for item in value:
        out.append(capo_backup.types.scan_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanJobSummaryList:
    import capo_backup.types.scan_job_summary

    out: ScanJobSummaryList = []
    for item in data:
        out.append(capo_backup.types.scan_job_summary.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.export_job_summary

ExportJobSummaries: TypeAlias = list[
    "capo_backupsearch.types.export_job_summary.ExportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobSummaries) -> list:
    import capo_backupsearch.types.export_job_summary

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.export_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportJobSummaries:
    import capo_backupsearch.types.export_job_summary

    out: ExportJobSummaries = []
    for item in data:
        out.append(capo_backupsearch.types.export_job_summary.deserialize_json(item))
    return out

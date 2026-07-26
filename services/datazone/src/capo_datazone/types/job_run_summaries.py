"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.job_run_summary

JobRunSummaries: TypeAlias = list["capo_datazone.types.job_run_summary.JobRunSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunSummaries) -> list:
    import capo_datazone.types.job_run_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.job_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRunSummaries:
    import capo_datazone.types.job_run_summary

    out: JobRunSummaries = []
    for item in data:
        out.append(capo_datazone.types.job_run_summary.deserialize_json(item))
    return out

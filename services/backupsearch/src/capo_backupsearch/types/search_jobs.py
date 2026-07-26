"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.search_job_summary

SearchJobs: TypeAlias = list[
    "capo_backupsearch.types.search_job_summary.SearchJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobs) -> list:
    import capo_backupsearch.types.search_job_summary

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.search_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchJobs:
    import capo_backupsearch.types.search_job_summary

    out: SearchJobs = []
    for item in data:
        out.append(capo_backupsearch.types.search_job_summary.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.sync_job_summary

SyncJobSummaries: TypeAlias = list[
    "capo_iottwinmaker.types.sync_job_summary.SyncJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SyncJobSummaries) -> list:
    import capo_iottwinmaker.types.sync_job_summary

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.sync_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SyncJobSummaries:
    import capo_iottwinmaker.types.sync_job_summary

    out: SyncJobSummaries = []
    for item in data:
        out.append(capo_iottwinmaker.types.sync_job_summary.deserialize_json(item))
    return out

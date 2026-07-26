"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.job_summary

JobSummaries: TypeAlias = list["capo_iotsitewise.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobSummaries) -> list:
    import capo_iotsitewise.types.job_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSummaries:
    import capo_iotsitewise.types.job_summary

    out: JobSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.job_summary.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.job_summary

JobList: TypeAlias = list["capo_entityresolution.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobList) -> list:
    import capo_entityresolution.types.job_summary

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobList:
    import capo_entityresolution.types.job_summary

    out: JobList = []
    for item in data:
        out.append(capo_entityresolution.types.job_summary.deserialize_json(item))
    return out

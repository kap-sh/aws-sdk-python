"""Generated from Smithy shape ``com.amazonaws.wisdom#ImportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.import_job_summary

ImportJobList: TypeAlias = list["capo_wisdom.types.import_job_summary.ImportJobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobList) -> list:
    import capo_wisdom.types.import_job_summary

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.import_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportJobList:
    import capo_wisdom.types.import_job_summary

    out: ImportJobList = []
    for item in data:
        out.append(capo_wisdom.types.import_job_summary.deserialize_json(item))
    return out

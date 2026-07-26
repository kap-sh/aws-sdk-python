"""Generated from Smithy shape ``com.amazonaws.databrew#JobRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.job_run

JobRunList: TypeAlias = list["capo_databrew.types.job_run.JobRun"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunList) -> list:
    import capo_databrew.types.job_run

    out: list = []
    for item in value:
        out.append(capo_databrew.types.job_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRunList:
    import capo_databrew.types.job_run

    out: JobRunList = []
    for item in data:
        out.append(capo_databrew.types.job_run.deserialize_json(item))
    return out

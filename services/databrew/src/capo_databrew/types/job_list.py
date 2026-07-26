"""Generated from Smithy shape ``com.amazonaws.databrew#JobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.job

JobList: TypeAlias = list["capo_databrew.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobList) -> list:
    import capo_databrew.types.job

    out: list = []
    for item in value:
        out.append(capo_databrew.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobList:
    import capo_databrew.types.job

    out: JobList = []
    for item in data:
        out.append(capo_databrew.types.job.deserialize_json(item))
    return out

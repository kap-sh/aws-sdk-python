"""Generated from Smithy shape ``com.amazonaws.databrew#JobNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.job_name

JobNameList: TypeAlias = list["capo_databrew.types.job_name.JobName"]


# --- restJson1 ser/de ---
def serialize_json(value: JobNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> JobNameList:
    return list(data)

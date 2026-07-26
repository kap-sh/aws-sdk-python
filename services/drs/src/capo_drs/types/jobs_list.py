"""Generated from Smithy shape ``com.amazonaws.drs#JobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.job

JobsList: TypeAlias = list["capo_drs.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: JobsList) -> list:
    import capo_drs.types.job

    out: list = []
    for item in value:
        out.append(capo_drs.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobsList:
    import capo_drs.types.job

    out: JobsList = []
    for item in data:
        out.append(capo_drs.types.job.deserialize_json(item))
    return out

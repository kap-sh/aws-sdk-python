"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#JobStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.job_state

JobStates: TypeAlias = list["capo_codeguru_reviewer.types.job_state.JobState"]


# --- restJson1 ser/de ---
def serialize_json(value: JobStates) -> list:
    import capo_codeguru_reviewer.types.job_state

    out: list = []
    for item in value:
        out.append(capo_codeguru_reviewer.types.job_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobStates:
    import capo_codeguru_reviewer.types.job_state

    out: JobStates = []
    for item in data:
        out.append(capo_codeguru_reviewer.types.job_state.deserialize_json(item))
    return out

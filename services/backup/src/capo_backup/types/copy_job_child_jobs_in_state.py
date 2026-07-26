"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobChildJobsInState``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.copy_job_state
    import capo_backup.types.long

CopyJobChildJobsInState: TypeAlias = dict[
    "capo_backup.types.copy_job_state.CopyJobState", "capo_backup.types.long.Long"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CopyJobChildJobsInState) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_backup.types.copy_job_state

        out[capo_backup.types.copy_job_state.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> CopyJobChildJobsInState:
    out: CopyJobChildJobsInState = {}
    for key, value in data.items():
        import capo_backup.types.copy_job_state

        out[capo_backup.types.copy_job_state.deserialize_json(key)] = value
    return out

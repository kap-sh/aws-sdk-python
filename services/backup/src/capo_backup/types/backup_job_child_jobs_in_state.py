"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobChildJobsInState``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_job_state
    import capo_backup.types.long

BackupJobChildJobsInState: TypeAlias = dict[
    "capo_backup.types.backup_job_state.BackupJobState", "capo_backup.types.long.Long"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BackupJobChildJobsInState) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_backup.types.backup_job_state

        out[capo_backup.types.backup_job_state.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> BackupJobChildJobsInState:
    out: BackupJobChildJobsInState = {}
    for key, value in data.items():
        import capo_backup.types.backup_job_state

        out[capo_backup.types.backup_job_state.deserialize_json(key)] = value
    return out

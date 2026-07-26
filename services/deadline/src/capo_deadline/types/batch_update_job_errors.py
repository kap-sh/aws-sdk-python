"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_job_error

BatchUpdateJobErrors: TypeAlias = list[
    "capo_deadline.types.batch_update_job_error.BatchUpdateJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobErrors) -> list:
    import capo_deadline.types.batch_update_job_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_update_job_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUpdateJobErrors:
    import capo_deadline.types.batch_update_job_error

    out: BatchUpdateJobErrors = []
    for item in data:
        out.append(capo_deadline.types.batch_update_job_error.deserialize_json(item))
    return out

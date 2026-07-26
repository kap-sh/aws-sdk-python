"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_job_error

BatchGetJobErrors: TypeAlias = list[
    "capo_deadline.types.batch_get_job_error.BatchGetJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobErrors) -> list:
    import capo_deadline.types.batch_get_job_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_job_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobErrors:
    import capo_deadline.types.batch_get_job_error

    out: BatchGetJobErrors = []
    for item in data:
        out.append(capo_deadline.types.batch_get_job_error.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_worker_error

BatchGetWorkerErrors: TypeAlias = list[
    "capo_deadline.types.batch_get_worker_error.BatchGetWorkerError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerErrors) -> list:
    import capo_deadline.types.batch_get_worker_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_worker_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetWorkerErrors:
    import capo_deadline.types.batch_get_worker_error

    out: BatchGetWorkerErrors = []
    for item in data:
        out.append(capo_deadline.types.batch_get_worker_error.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_task_error

BatchGetTaskErrors: TypeAlias = list[
    "capo_deadline.types.batch_get_task_error.BatchGetTaskError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskErrors) -> list:
    import capo_deadline.types.batch_get_task_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetTaskErrors:
    import capo_deadline.types.batch_get_task_error

    out: BatchGetTaskErrors = []
    for item in data:
        out.append(capo_deadline.types.batch_get_task_error.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_step_error

BatchGetStepErrors: TypeAlias = list[
    "capo_deadline.types.batch_get_step_error.BatchGetStepError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepErrors) -> list:
    import capo_deadline.types.batch_get_step_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_step_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetStepErrors:
    import capo_deadline.types.batch_get_step_error

    out: BatchGetStepErrors = []
    for item in data:
        out.append(capo_deadline.types.batch_get_step_error.deserialize_json(item))
    return out

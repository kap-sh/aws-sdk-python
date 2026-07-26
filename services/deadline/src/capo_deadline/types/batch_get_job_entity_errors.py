"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.get_job_entity_error

BatchGetJobEntityErrors: TypeAlias = list[
    "capo_deadline.types.get_job_entity_error.GetJobEntityError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityErrors) -> list:
    import capo_deadline.types.get_job_entity_error

    out: list = []
    for item in value:
        out.append(capo_deadline.types.get_job_entity_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobEntityErrors:
    import capo_deadline.types.get_job_entity_error

    out: BatchGetJobEntityErrors = []
    for item in data:
        out.append(capo_deadline.types.get_job_entity_error.deserialize_json(item))
    return out

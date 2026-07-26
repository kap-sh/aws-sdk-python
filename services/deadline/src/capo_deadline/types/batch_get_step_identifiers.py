"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_step_identifier

BatchGetStepIdentifiers: TypeAlias = list[
    "capo_deadline.types.batch_get_step_identifier.BatchGetStepIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepIdentifiers) -> list:
    import capo_deadline.types.batch_get_step_identifier

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_step_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetStepIdentifiers:
    import capo_deadline.types.batch_get_step_identifier

    out: BatchGetStepIdentifiers = []
    for item in data:
        out.append(capo_deadline.types.batch_get_step_identifier.deserialize_json(item))
    return out

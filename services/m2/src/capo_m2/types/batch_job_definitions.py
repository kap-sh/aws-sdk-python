"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.batch_job_definition

BatchJobDefinitions: TypeAlias = list[
    "capo_m2.types.batch_job_definition.BatchJobDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobDefinitions) -> list:
    import capo_m2.types.batch_job_definition

    out: list = []
    for item in value:
        out.append(capo_m2.types.batch_job_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchJobDefinitions:
    import capo_m2.types.batch_job_definition

    out: BatchJobDefinitions = []
    for item in data:
        out.append(capo_m2.types.batch_job_definition.deserialize_json(item))
    return out

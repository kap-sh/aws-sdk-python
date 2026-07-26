"""Generated from Smithy shape ``com.amazonaws.pipes#BatchDependsOn``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.batch_job_dependency

BatchDependsOn: TypeAlias = list[
    "capo_pipes.types.batch_job_dependency.BatchJobDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDependsOn) -> list:
    import capo_pipes.types.batch_job_dependency

    out: list = []
    for item in value:
        out.append(capo_pipes.types.batch_job_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDependsOn:
    import capo_pipes.types.batch_job_dependency

    out: BatchDependsOn = []
    for item in data:
        out.append(capo_pipes.types.batch_job_dependency.deserialize_json(item))
    return out

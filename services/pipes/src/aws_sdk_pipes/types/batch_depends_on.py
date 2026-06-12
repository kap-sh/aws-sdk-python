"""Generated from Smithy shape ``com.amazonaws.pipes#BatchDependsOn``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_job_dependency

BatchDependsOn: TypeAlias = list[
    "aws_sdk_pipes.types.batch_job_dependency.BatchJobDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDependsOn) -> list:
    import aws_sdk_pipes.types.batch_job_dependency

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.batch_job_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDependsOn:
    import aws_sdk_pipes.types.batch_job_dependency

    out: BatchDependsOn = []
    for item in data:
        out.append(aws_sdk_pipes.types.batch_job_dependency.deserialize_json(item))
    return out

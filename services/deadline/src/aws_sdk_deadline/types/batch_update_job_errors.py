"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_job_error

BatchUpdateJobErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_update_job_error.BatchUpdateJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobErrors) -> list:
    import aws_sdk_deadline.types.batch_update_job_error

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_update_job_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUpdateJobErrors:
    import aws_sdk_deadline.types.batch_update_job_error

    out: BatchUpdateJobErrors = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_update_job_error.deserialize_json(item))
    return out

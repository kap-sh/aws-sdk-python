"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_error

BatchGetWorkerErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_worker_error.BatchGetWorkerError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerErrors) -> list:
    import aws_sdk_deadline.types.batch_get_worker_error

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_worker_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetWorkerErrors:
    import aws_sdk_deadline.types.batch_get_worker_error

    out: BatchGetWorkerErrors = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_get_worker_error.deserialize_json(item))
    return out

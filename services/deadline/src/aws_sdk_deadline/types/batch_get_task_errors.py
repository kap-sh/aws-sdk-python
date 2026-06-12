"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_task_error

BatchGetTaskErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_task_error.BatchGetTaskError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskErrors) -> list:
    import aws_sdk_deadline.types.batch_get_task_error

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetTaskErrors:
    import aws_sdk_deadline.types.batch_get_task_error

    out: BatchGetTaskErrors = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_get_task_error.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_task_error

BatchUpdateTaskErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_update_task_error.BatchUpdateTaskError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskErrors) -> list:
    import aws_sdk_deadline.types.batch_update_task_error

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_update_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUpdateTaskErrors:
    import aws_sdk_deadline.types.batch_update_task_error

    out: BatchUpdateTaskErrors = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_update_task_error.deserialize_json(item)
        )
    return out

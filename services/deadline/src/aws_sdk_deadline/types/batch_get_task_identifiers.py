"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_task_identifier

BatchGetTaskIdentifiers: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_task_identifier.BatchGetTaskIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskIdentifiers) -> list:
    import aws_sdk_deadline.types.batch_get_task_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.batch_get_task_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetTaskIdentifiers:
    import aws_sdk_deadline.types.batch_get_task_identifier

    out: BatchGetTaskIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_task_identifier.deserialize_json(item)
        )
    return out

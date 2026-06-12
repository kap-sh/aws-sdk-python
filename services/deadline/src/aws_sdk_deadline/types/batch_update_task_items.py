"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_task_item

BatchUpdateTaskItems: TypeAlias = list[
    "aws_sdk_deadline.types.batch_update_task_item.BatchUpdateTaskItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskItems) -> list:
    import aws_sdk_deadline.types.batch_update_task_item

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_update_task_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUpdateTaskItems:
    import aws_sdk_deadline.types.batch_update_task_item

    out: BatchUpdateTaskItems = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_update_task_item.deserialize_json(item))
    return out

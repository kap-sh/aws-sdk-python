"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_step_item

BatchGetStepItems: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_step_item.BatchGetStepItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepItems) -> list:
    import aws_sdk_deadline.types.batch_get_step_item

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_step_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetStepItems:
    import aws_sdk_deadline.types.batch_get_step_item

    out: BatchGetStepItems = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_get_step_item.deserialize_json(item))
    return out

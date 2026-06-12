"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_item

BatchGetWorkerItems: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_worker_item.BatchGetWorkerItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerItems) -> list:
    import aws_sdk_deadline.types.batch_get_worker_item

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_worker_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetWorkerItems:
    import aws_sdk_deadline.types.batch_get_worker_item

    out: BatchGetWorkerItems = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_get_worker_item.deserialize_json(item))
    return out

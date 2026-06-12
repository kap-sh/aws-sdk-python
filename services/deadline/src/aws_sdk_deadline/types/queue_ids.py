"""Generated from Smithy shape ``com.amazonaws.deadline#QueueIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_id

QueueIds: TypeAlias = list["aws_sdk_deadline.types.queue_id.QueueId"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueIds) -> list:
    return list(value)


def deserialize_json(data: list) -> QueueIds:
    return list(data)

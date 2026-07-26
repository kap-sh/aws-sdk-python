"""Generated from Smithy shape ``com.amazonaws.connect#Queues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.queue_id

Queues: TypeAlias = list["capo_connect.types.queue_id.QueueId"]


# --- restJson1 ser/de ---
def serialize_json(value: Queues) -> list:
    return list(value)


def deserialize_json(data: list) -> Queues:
    return list(data)

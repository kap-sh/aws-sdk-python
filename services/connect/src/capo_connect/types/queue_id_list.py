"""Generated from Smithy shape ``com.amazonaws.connect#QueueIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.queue_id

QueueIdList: TypeAlias = list["capo_connect.types.queue_id.QueueId"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> QueueIdList:
    return list(data)

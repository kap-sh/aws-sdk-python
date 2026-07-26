"""Generated from Smithy shape ``com.amazonaws.connect#AssociatedQueueIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.queue_id

AssociatedQueueIdList: TypeAlias = list["capo_connect.types.queue_id.QueueId"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedQueueIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedQueueIdList:
    return list(data)

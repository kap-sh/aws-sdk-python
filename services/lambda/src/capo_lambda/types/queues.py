"""Generated from Smithy shape ``com.amazonaws.lambda#Queues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.queue

Queues: TypeAlias = list["capo_lambda.types.queue.Queue"]


# --- restJson1 ser/de ---
def serialize_json(value: Queues) -> list:
    return list(value)


def deserialize_json(data: list) -> Queues:
    return [item for item in data if item is not None]

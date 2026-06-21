"""Generated from Smithy shape ``com.amazonaws.outposts#OrderStatus``."""

from typing import Literal, TypeAlias, cast

OrderStatus: TypeAlias = Literal[
    "RECEIVED",
    "PENDING",
    "PROCESSING",
    "INSTALLING",
    "FULFILLED",
    "CANCELLED",
    "PREPARING",
    "IN_PROGRESS",
    "DELIVERED",
    "COMPLETED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderStatus:
    return cast(OrderStatus, data)

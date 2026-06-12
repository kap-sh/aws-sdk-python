"""Generated from Smithy shape ``com.amazonaws.outposts#OrderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: OrderStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderStatus value: {data!r}")
    return cast(OrderStatus, data)

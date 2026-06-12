"""Generated from Smithy shape ``com.amazonaws.outposts#OrderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

OrderType: TypeAlias = Literal[
    "OUTPOST",
    "REPLACEMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUTPOST",
        "REPLACEMENT",
    )
)


def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderType value: {data!r}")
    return cast(OrderType, data)

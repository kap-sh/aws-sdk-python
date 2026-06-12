"""Generated from Smithy shape ``com.amazonaws.databrew#Order``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

Order: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DESCENDING",
        "ASCENDING",
    )
)


def serialize_json(value: Order) -> str:
    return value


def deserialize_json(data: str) -> Order:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Order value: {data!r}")
    return cast(Order, data)

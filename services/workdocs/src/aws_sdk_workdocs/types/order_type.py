"""Generated from Smithy shape ``com.amazonaws.workdocs#OrderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

OrderType: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderType value: {data!r}")
    return cast(OrderType, data)

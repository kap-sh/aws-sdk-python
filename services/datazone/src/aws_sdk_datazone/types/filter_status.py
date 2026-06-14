"""Generated from Smithy shape ``com.amazonaws.datazone#FilterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

FilterStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
    )
)


def serialize_json(value: FilterStatus) -> str:
    return value


def deserialize_json(data: str) -> FilterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterStatus value: {data!r}")
    return cast(FilterStatus, data)

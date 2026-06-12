"""Generated from Smithy shape ``com.amazonaws.connect#Unit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Unit: TypeAlias = Literal[
    "SECONDS",
    "COUNT",
    "PERCENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECONDS",
        "COUNT",
        "PERCENT",
    )
)


def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Unit value: {data!r}")
    return cast(Unit, data)

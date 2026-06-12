"""Generated from Smithy shape ``com.amazonaws.pinpoint#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Mode: TypeAlias = Literal[
    "DELIVERY",
    "FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELIVERY",
        "FILTER",
    )
)


def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {data!r}")
    return cast(Mode, data)

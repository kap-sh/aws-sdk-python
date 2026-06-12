"""Generated from Smithy shape ``com.amazonaws.medialive#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Placeholder documentation for ConnectionMode"""
ConnectionMode: TypeAlias = Literal[
    "CALLER",
    "LISTENER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CALLER",
        "LISTENER",
    )
)


def serialize_json(value: ConnectionMode) -> str:
    return value


def deserialize_json(data: str) -> ConnectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionMode value: {data!r}")
    return cast(ConnectionMode, data)

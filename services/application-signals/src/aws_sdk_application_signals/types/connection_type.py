"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "INDIRECT",
    "DIRECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDIRECT",
        "DIRECT",
    )
)


def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)

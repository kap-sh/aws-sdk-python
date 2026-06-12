"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

ConnectionMode: TypeAlias = Literal[
    "Public",
    "Private",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Public",
        "Private",
    )
)


def serialize_json(value: ConnectionMode) -> str:
    return value


def deserialize_json(data: str) -> ConnectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionMode value: {data!r}")
    return cast(ConnectionMode, data)

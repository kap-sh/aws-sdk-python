"""Generated from Smithy shape ``com.amazonaws.connect#Channel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Channel: TypeAlias = Literal[
    "VOICE",
    "CHAT",
    "TASK",
    "EMAIL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOICE",
        "CHAT",
        "TASK",
        "EMAIL",
    )
)


def serialize_json(value: Channel) -> str:
    return value


def deserialize_json(data: str) -> Channel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Channel value: {data!r}")
    return cast(Channel, data)

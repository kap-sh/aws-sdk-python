"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ParticipantTimerType: TypeAlias = Literal[
    "IDLE",
    "DISCONNECT_NONCUSTOMER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "DISCONNECT_NONCUSTOMER",
    )
)


def serialize_json(value: ParticipantTimerType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantTimerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantTimerType value: {data!r}")
    return cast(ParticipantTimerType, data)

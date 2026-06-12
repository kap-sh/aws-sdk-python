"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ParticipantTimerAction: TypeAlias = Literal["Unset",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Unset",))


def serialize_json(value: ParticipantTimerAction) -> str:
    return value


def deserialize_json(data: str) -> ParticipantTimerAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantTimerAction value: {data!r}")
    return cast(ParticipantTimerAction, data)

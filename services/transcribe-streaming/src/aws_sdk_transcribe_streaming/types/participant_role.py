"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ParticipantRole: TypeAlias = Literal[
    "AGENT",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "CUSTOMER",
    )
)


def serialize_json(value: ParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> ParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantRole value: {data!r}")
    return cast(ParticipantRole, data)

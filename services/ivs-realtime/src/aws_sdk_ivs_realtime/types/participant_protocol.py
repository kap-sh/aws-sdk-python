"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

ParticipantProtocol: TypeAlias = Literal[
    "UNKNOWN",
    "WHIP",
    "RTMP",
    "RTMPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "WHIP",
        "RTMP",
        "RTMPS",
    )
)


def serialize_json(value: ParticipantProtocol) -> str:
    return value


def deserialize_json(data: str) -> ParticipantProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantProtocol value: {data!r}")
    return cast(ParticipantProtocol, data)

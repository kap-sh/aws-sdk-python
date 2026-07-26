"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantProtocol``."""

from typing import Literal, TypeAlias, cast

ParticipantProtocol: TypeAlias = Literal[
    "UNKNOWN",
    "WHIP",
    "RTMP",
    "RTMPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantProtocol) -> str:
    return value


def deserialize_json(data: str) -> ParticipantProtocol:
    return cast(ParticipantProtocol, data)

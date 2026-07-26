"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerType``."""

from typing import Literal, TypeAlias, cast

ParticipantTimerType: TypeAlias = Literal[
    "IDLE",
    "DISCONNECT_NONCUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantTimerType:
    return cast(ParticipantTimerType, data)

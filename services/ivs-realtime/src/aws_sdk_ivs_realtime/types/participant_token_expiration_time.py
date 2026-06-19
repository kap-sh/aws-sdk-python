"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenExpirationTime``."""

import datetime
from typing import TypeAlias

ParticipantTokenExpirationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenExpirationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> ParticipantTokenExpirationTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

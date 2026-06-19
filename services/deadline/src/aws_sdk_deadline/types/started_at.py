"""Generated from Smithy shape ``com.amazonaws.deadline#StartedAt``."""

import datetime
from typing import TypeAlias

StartedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartedAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> StartedAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

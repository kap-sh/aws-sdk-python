"""Generated from Smithy shape ``com.amazonaws.deadline#StartsAt``."""

import datetime
from typing import TypeAlias

StartsAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartsAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> StartsAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

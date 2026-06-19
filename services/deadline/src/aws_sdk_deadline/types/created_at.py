"""Generated from Smithy shape ``com.amazonaws.deadline#CreatedAt``."""

import datetime
from typing import TypeAlias

CreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> CreatedAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

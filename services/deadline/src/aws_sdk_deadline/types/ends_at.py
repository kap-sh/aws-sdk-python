"""Generated from Smithy shape ``com.amazonaws.deadline#EndsAt``."""

import datetime
from typing import TypeAlias

EndsAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: EndsAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> EndsAt:
    return datetime.datetime.fromisoformat(data)

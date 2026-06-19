"""Generated from Smithy shape ``com.amazonaws.deadline#EndedAt``."""

import datetime
from typing import TypeAlias

EndedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: EndedAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> EndedAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

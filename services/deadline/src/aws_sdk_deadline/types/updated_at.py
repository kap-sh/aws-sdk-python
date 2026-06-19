"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedAt``."""

import datetime
from typing import TypeAlias

UpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAt) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> UpdatedAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

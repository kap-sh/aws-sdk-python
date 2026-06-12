"""Generated from Smithy shape ``com.amazonaws.codecatalyst#Timestamp``."""

import datetime
from typing import TypeAlias

Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Timestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Timestamp:
    return datetime.datetime.fromisoformat(data)

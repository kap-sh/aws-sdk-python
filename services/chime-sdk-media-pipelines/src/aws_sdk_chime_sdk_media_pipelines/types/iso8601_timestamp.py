"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#Iso8601Timestamp``."""

import datetime
from typing import TypeAlias

Iso8601Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601Timestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Iso8601Timestamp:
    return datetime.datetime.fromisoformat(data)

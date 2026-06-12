"""Generated from Smithy shape ``com.amazonaws.artifact#TimestampAttribute``."""

import datetime
from typing import TypeAlias

TimestampAttribute: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimestampAttribute) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> TimestampAttribute:
    return datetime.datetime.fromisoformat(data)

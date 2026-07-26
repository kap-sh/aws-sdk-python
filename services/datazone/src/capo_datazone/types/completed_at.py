"""Generated from Smithy shape ``com.amazonaws.datazone#CompletedAt``."""

import datetime
from typing import TypeAlias

CompletedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CompletedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CompletedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

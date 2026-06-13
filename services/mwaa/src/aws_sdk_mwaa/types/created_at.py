"""Generated from Smithy shape ``com.amazonaws.mwaa#CreatedAt``."""

import datetime
from typing import TypeAlias

CreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

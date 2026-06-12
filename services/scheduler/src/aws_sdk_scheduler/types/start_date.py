"""Generated from Smithy shape ``com.amazonaws.scheduler#StartDate``."""

import datetime
from typing import TypeAlias

StartDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> StartDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

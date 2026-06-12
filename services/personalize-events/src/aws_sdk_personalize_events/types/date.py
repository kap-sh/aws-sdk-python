"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Date``."""

import datetime
from typing import TypeAlias

Date: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Date) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Date:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

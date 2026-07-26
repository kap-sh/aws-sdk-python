"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#TimeStamp``."""

import datetime
from typing import TypeAlias

TimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimeStamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> TimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

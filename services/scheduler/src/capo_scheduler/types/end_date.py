"""Generated from Smithy shape ``com.amazonaws.scheduler#EndDate``."""

import datetime
from typing import TypeAlias

EndDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: EndDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> EndDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

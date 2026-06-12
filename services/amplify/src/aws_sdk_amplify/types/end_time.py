"""Generated from Smithy shape ``com.amazonaws.amplify#EndTime``."""

import datetime
from typing import TypeAlias

EndTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: EndTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> EndTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

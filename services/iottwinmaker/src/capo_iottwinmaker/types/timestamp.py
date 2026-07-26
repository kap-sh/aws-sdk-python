"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Timestamp``."""

import datetime
from typing import TypeAlias

"""supports epoch seconds value"""
Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

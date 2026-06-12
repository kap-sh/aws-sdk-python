"""Generated from Smithy shape ``com.amazonaws.medialive#__timestamp``."""

import datetime
from typing import TypeAlias

"""Placeholder documentation for __timestamp"""
__timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> __timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

"""Generated from Smithy shape ``com.amazonaws.simpledbv2#RequestedAt``."""

import datetime
from typing import TypeAlias

"""Timestamp when the export (or any other operation) was requested."""
RequestedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RequestedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> RequestedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

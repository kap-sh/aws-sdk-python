"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreatedAt``."""

import datetime
from typing import TypeAlias

"""<p>Created at timestamp for the resource.</p>"""
CreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

"""Generated from Smithy shape ``com.amazonaws.ivs#Time``."""

import datetime
from typing import TypeAlias

Time: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Time) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Time:
    return datetime.datetime.fromisoformat(data)

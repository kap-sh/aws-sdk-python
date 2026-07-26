"""Generated from Smithy shape ``com.amazonaws.iotwireless#LastUpdateTime``."""

import datetime
from typing import TypeAlias

LastUpdateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> LastUpdateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

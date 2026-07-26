"""Generated from Smithy shape ``com.amazonaws.notifications#LastActivationTime``."""

import datetime
from typing import TypeAlias

LastActivationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastActivationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> LastActivationTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

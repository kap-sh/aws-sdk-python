"""Generated from Smithy shape ``com.amazonaws.ivs#StreamStartTime``."""

import datetime
from typing import TypeAlias

StreamStartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StreamStartTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> StreamStartTime:
    return datetime.datetime.fromisoformat(data)

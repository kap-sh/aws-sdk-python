"""Generated from Smithy shape ``com.amazonaws.connectcases#CreatedTime``."""

import datetime
from typing import TypeAlias

CreatedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> CreatedTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

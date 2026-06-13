"""Generated from Smithy shape ``com.amazonaws.connectcases#ConnectedToSystemTime``."""

import datetime
from typing import TypeAlias

ConnectedToSystemTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ConnectedToSystemTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> ConnectedToSystemTime:
    return datetime.datetime.fromisoformat(data)

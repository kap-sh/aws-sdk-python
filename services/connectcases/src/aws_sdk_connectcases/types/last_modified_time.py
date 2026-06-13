"""Generated from Smithy shape ``com.amazonaws.connectcases#LastModifiedTime``."""

import datetime
from typing import TypeAlias

LastModifiedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModifiedTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> LastModifiedTime:
    return datetime.datetime.fromisoformat(data)

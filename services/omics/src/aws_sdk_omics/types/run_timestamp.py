"""Generated from Smithy shape ``com.amazonaws.omics#RunTimestamp``."""

import datetime
from typing import TypeAlias

RunTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RunTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> RunTimestamp:
    return datetime.datetime.fromisoformat(data)

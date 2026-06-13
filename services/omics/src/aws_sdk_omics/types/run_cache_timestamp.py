"""Generated from Smithy shape ``com.amazonaws.omics#RunCacheTimestamp``."""

import datetime
from typing import TypeAlias

RunCacheTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RunCacheTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> RunCacheTimestamp:
    return datetime.datetime.fromisoformat(data)

"""Generated from Smithy shape ``com.amazonaws.omics#RunGroupTimestamp``."""

import datetime
from typing import TypeAlias

RunGroupTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RunGroupTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> RunGroupTimestamp:
    return datetime.datetime.fromisoformat(data)

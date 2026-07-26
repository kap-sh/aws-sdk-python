"""Generated from Smithy shape ``com.amazonaws.omics#TaskTimestamp``."""

import datetime
from typing import TypeAlias

TaskTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TaskTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> TaskTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

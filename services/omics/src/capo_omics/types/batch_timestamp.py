"""Generated from Smithy shape ``com.amazonaws.omics#BatchTimestamp``."""

import datetime
from typing import TypeAlias

BatchTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: BatchTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> BatchTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

"""Generated from Smithy shape ``com.amazonaws.novaact#DateTimestamp``."""

import datetime
from typing import TypeAlias

DateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> DateTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DateTimestamp``."""

import datetime
from typing import TypeAlias

"""Time Stamp."""
DateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> DateTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

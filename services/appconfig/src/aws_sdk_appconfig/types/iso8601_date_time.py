"""Generated from Smithy shape ``com.amazonaws.appconfig#Iso8601DateTime``."""

import datetime
from typing import TypeAlias

Iso8601DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601DateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Iso8601DateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

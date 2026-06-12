"""Generated from Smithy shape ``com.amazonaws.appfabric#DateTime``."""

import datetime
from typing import TypeAlias

DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> DateTime:
    return datetime.datetime.fromisoformat(data)

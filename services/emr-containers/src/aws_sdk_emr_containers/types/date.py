"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Date``."""

import datetime
from typing import TypeAlias

Date: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Date) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Date:
    return datetime.datetime.fromisoformat(data)

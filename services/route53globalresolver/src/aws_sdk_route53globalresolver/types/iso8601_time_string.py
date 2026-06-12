"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ISO8601TimeString``."""

import datetime
from typing import TypeAlias

ISO8601TimeString: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ISO8601TimeString) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> ISO8601TimeString:
    return datetime.datetime.fromisoformat(data)

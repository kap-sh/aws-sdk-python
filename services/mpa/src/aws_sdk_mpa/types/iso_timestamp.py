"""Generated from Smithy shape ``com.amazonaws.mpa#IsoTimestamp``."""

import datetime
from typing import TypeAlias

IsoTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: IsoTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> IsoTimestamp:
    return datetime.datetime.fromisoformat(data)

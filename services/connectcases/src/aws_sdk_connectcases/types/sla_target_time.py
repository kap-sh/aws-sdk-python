"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaTargetTime``."""

import datetime
from typing import TypeAlias

SlaTargetTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SlaTargetTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> SlaTargetTime:
    return datetime.datetime.fromisoformat(data)

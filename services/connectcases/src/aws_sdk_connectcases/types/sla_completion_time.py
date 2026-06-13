"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaCompletionTime``."""

import datetime
from typing import TypeAlias

SlaCompletionTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SlaCompletionTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> SlaCompletionTime:
    return datetime.datetime.fromisoformat(data)

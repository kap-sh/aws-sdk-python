"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#CreationTime``."""

import datetime
from typing import TypeAlias

CreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> CreationTime:
    return datetime.datetime.fromisoformat(data)

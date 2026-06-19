"""Generated from Smithy shape ``com.amazonaws.omics#UpdateTime``."""

import datetime
from typing import TypeAlias

UpdateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> UpdateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

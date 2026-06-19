"""Generated from Smithy shape ``com.amazonaws.omics#CompletionTime``."""

import datetime
from typing import TypeAlias

CompletionTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CompletionTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> CompletionTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))

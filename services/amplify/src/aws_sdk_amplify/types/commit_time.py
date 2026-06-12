"""Generated from Smithy shape ``com.amazonaws.amplify#CommitTime``."""

import datetime
from typing import TypeAlias

CommitTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CommitTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CommitTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentStartTime``."""

import datetime
from typing import TypeAlias

ExperimentStartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentStartTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ExperimentStartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionStartTime``."""

import datetime
from typing import TypeAlias

ExperimentActionStartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionStartTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ExperimentActionStartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

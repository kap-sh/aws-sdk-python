"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionEndTime``."""

import datetime
from typing import TypeAlias

ExperimentActionEndTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionEndTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ExperimentActionEndTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)

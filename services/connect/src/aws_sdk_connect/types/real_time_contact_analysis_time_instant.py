"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTimeInstant``."""

import datetime
from typing import TypeAlias

RealTimeContactAnalysisTimeInstant: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTimeInstant) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> RealTimeContactAnalysisTimeInstant:
    return datetime.datetime.fromisoformat(data)

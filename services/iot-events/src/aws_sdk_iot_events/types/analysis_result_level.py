"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResultLevel``."""

from typing import Literal, TypeAlias, cast

AnalysisResultLevel: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisResultLevel) -> str:
    return value


def deserialize_json(data: str) -> AnalysisResultLevel:
    return cast(AnalysisResultLevel, data)

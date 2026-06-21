"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

AnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalysisStatus:
    return cast(AnalysisStatus, data)

"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisStatus``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisStatus:
    return cast(RealTimeContactAnalysisStatus, data)

"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisOutputType``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisOutputType: TypeAlias = Literal[
    "Raw",
    "Redacted",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisOutputType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisOutputType:
    return cast(RealTimeContactAnalysisOutputType, data)

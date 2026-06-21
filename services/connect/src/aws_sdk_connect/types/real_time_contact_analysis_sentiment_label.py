"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSentimentLabel``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisSentimentLabel: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSentimentLabel) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSentimentLabel:
    return cast(RealTimeContactAnalysisSentimentLabel, data)

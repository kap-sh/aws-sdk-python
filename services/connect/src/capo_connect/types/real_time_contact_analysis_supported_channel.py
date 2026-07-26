"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSupportedChannel``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisSupportedChannel: TypeAlias = Literal[
    "VOICE",
    "CHAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSupportedChannel) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSupportedChannel:
    return cast(RealTimeContactAnalysisSupportedChannel, data)

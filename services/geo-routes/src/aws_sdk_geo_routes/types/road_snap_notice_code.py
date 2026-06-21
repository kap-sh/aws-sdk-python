"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapNoticeCode``."""

from typing import Literal, TypeAlias, cast

RoadSnapNoticeCode: TypeAlias = Literal[
    "TracePointsHeadingIgnored",
    "TracePointsIgnored",
    "TracePointsMovedByLargeDistance",
    "TracePointsNotMatched",
    "TracePointsOutOfSequence",
    "TracePointsSpeedEstimated",
    "TracePointsSpeedIgnored",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapNoticeCode:
    return cast(RoadSnapNoticeCode, data)

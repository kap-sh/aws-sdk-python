"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "TracePointsHeadingIgnored",
        "TracePointsIgnored",
        "TracePointsMovedByLargeDistance",
        "TracePointsNotMatched",
        "TracePointsOutOfSequence",
        "TracePointsSpeedEstimated",
        "TracePointsSpeedIgnored",
    )
)


def serialize_json(value: RoadSnapNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoadSnapNoticeCode value: {data!r}")
    return cast(RoadSnapNoticeCode, data)

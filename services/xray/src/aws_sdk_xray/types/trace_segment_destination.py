"""Generated from Smithy shape ``com.amazonaws.xray#TraceSegmentDestination``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

TraceSegmentDestination: TypeAlias = Literal[
    "XRay",
    "CloudWatchLogs",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "XRay",
        "CloudWatchLogs",
    )
)


def serialize_json(value: TraceSegmentDestination) -> str:
    return value


def deserialize_json(data: str) -> TraceSegmentDestination:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TraceSegmentDestination value: {data!r}")
    return cast(TraceSegmentDestination, data)

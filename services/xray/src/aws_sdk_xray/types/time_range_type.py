"""Generated from Smithy shape ``com.amazonaws.xray#TimeRangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

TimeRangeType: TypeAlias = Literal[
    "TraceId",
    "Event",
    "Service",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TraceId",
        "Event",
        "Service",
    )
)


def serialize_json(value: TimeRangeType) -> str:
    return value


def deserialize_json(data: str) -> TimeRangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeRangeType value: {data!r}")
    return cast(TimeRangeType, data)

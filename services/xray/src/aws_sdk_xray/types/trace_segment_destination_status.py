"""Generated from Smithy shape ``com.amazonaws.xray#TraceSegmentDestinationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

TraceSegmentDestinationStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
    )
)


def serialize_json(value: TraceSegmentDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> TraceSegmentDestinationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TraceSegmentDestinationStatus value: {data!r}"
        )
    return cast(TraceSegmentDestinationStatus, data)

"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduleAt``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ScheduleAt: TypeAlias = Literal[
    "NOW",
    "TIMESTAMP",
    "OFF_PEAK_WINDOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOW",
        "TIMESTAMP",
        "OFF_PEAK_WINDOW",
    )
)


def serialize_json(value: ScheduleAt) -> str:
    return value


def deserialize_json(data: str) -> ScheduleAt:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleAt value: {data!r}")
    return cast(ScheduleAt, data)

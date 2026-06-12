"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleEntryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

ScheduleEntryType: TypeAlias = Literal[
    "PROGRAM",
    "FILLER_SLATE",
    "ALTERNATE_MEDIA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROGRAM",
        "FILLER_SLATE",
        "ALTERNATE_MEDIA",
    )
)


def serialize_json(value: ScheduleEntryType) -> str:
    return value


def deserialize_json(data: str) -> ScheduleEntryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleEntryType value: {data!r}")
    return cast(ScheduleEntryType, data)

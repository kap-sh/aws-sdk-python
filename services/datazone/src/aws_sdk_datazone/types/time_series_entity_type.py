"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

TimeSeriesEntityType: TypeAlias = Literal[
    "ASSET",
    "LISTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "LISTING",
    )
)


def serialize_json(value: TimeSeriesEntityType) -> str:
    return value


def deserialize_json(data: str) -> TimeSeriesEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeSeriesEntityType value: {data!r}")
    return cast(TimeSeriesEntityType, data)

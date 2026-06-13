"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LineChartType: TypeAlias = Literal[
    "LINE",
    "AREA",
    "STACKED_AREA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "AREA",
        "STACKED_AREA",
    )
)


def serialize_json(value: LineChartType) -> str:
    return value


def deserialize_json(data: str) -> LineChartType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineChartType value: {data!r}")
    return cast(LineChartType, data)

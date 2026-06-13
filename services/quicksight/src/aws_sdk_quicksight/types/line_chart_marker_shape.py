"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartMarkerShape``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LineChartMarkerShape: TypeAlias = Literal[
    "CIRCLE",
    "TRIANGLE",
    "SQUARE",
    "DIAMOND",
    "ROUNDED_SQUARE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CIRCLE",
        "TRIANGLE",
        "SQUARE",
        "DIAMOND",
        "ROUNDED_SQUARE",
    )
)


def serialize_json(value: LineChartMarkerShape) -> str:
    return value


def deserialize_json(data: str) -> LineChartMarkerShape:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineChartMarkerShape value: {data!r}")
    return cast(LineChartMarkerShape, data)

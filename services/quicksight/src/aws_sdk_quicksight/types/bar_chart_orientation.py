"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartOrientation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BarChartOrientation: TypeAlias = Literal[
    "HORIZONTAL",
    "VERTICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HORIZONTAL",
        "VERTICAL",
    )
)


def serialize_json(value: BarChartOrientation) -> str:
    return value


def deserialize_json(data: str) -> BarChartOrientation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BarChartOrientation value: {data!r}")
    return cast(BarChartOrientation, data)

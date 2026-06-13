"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartLineStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LineChartLineStyle: TypeAlias = Literal[
    "SOLID",
    "DOTTED",
    "DASHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLID",
        "DOTTED",
        "DASHED",
    )
)


def serialize_json(value: LineChartLineStyle) -> str:
    return value


def deserialize_json(data: str) -> LineChartLineStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineChartLineStyle value: {data!r}")
    return cast(LineChartLineStyle, data)

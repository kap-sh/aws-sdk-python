"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotFillStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BoxPlotFillStyle: TypeAlias = Literal[
    "SOLID",
    "TRANSPARENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLID",
        "TRANSPARENT",
    )
)


def serialize_json(value: BoxPlotFillStyle) -> str:
    return value


def deserialize_json(data: str) -> BoxPlotFillStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BoxPlotFillStyle value: {data!r}")
    return cast(BoxPlotFillStyle, data)

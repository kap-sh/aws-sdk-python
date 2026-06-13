"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramBinType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

HistogramBinType: TypeAlias = Literal[
    "BIN_COUNT",
    "BIN_WIDTH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BIN_COUNT",
        "BIN_WIDTH",
    )
)


def serialize_json(value: HistogramBinType) -> str:
    return value


def deserialize_json(data: str) -> HistogramBinType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HistogramBinType value: {data!r}")
    return cast(HistogramBinType, data)

"""Generated from Smithy shape ``com.amazonaws.quicksight#StyledCellType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

StyledCellType: TypeAlias = Literal[
    "TOTAL",
    "METRIC_HEADER",
    "VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOTAL",
        "METRIC_HEADER",
        "VALUE",
    )
)


def serialize_json(value: StyledCellType) -> str:
    return value


def deserialize_json(data: str) -> StyledCellType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StyledCellType value: {data!r}")
    return cast(StyledCellType, data)

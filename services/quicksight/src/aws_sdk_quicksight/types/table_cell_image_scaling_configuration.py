"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellImageScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableCellImageScalingConfiguration: TypeAlias = Literal[
    "FIT_TO_CELL_HEIGHT",
    "FIT_TO_CELL_WIDTH",
    "DO_NOT_SCALE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIT_TO_CELL_HEIGHT",
        "FIT_TO_CELL_WIDTH",
        "DO_NOT_SCALE",
    )
)


def serialize_json(value: TableCellImageScalingConfiguration) -> str:
    return value


def deserialize_json(data: str) -> TableCellImageScalingConfiguration:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TableCellImageScalingConfiguration value: {data!r}"
        )
    return cast(TableCellImageScalingConfiguration, data)

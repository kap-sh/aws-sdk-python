"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellImageScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

TableCellImageScalingConfiguration: TypeAlias = Literal[
    "FIT_TO_CELL_HEIGHT",
    "FIT_TO_CELL_WIDTH",
    "DO_NOT_SCALE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableCellImageScalingConfiguration) -> str:
    return value


def deserialize_json(data: str) -> TableCellImageScalingConfiguration:
    return cast(TableCellImageScalingConfiguration, data)

"""Generated from Smithy shape ``com.amazonaws.quicksight#StyledCellType``."""

from typing import Literal, TypeAlias, cast

StyledCellType: TypeAlias = Literal[
    "TOTAL",
    "METRIC_HEADER",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StyledCellType) -> str:
    return value


def deserialize_json(data: str) -> StyledCellType:
    return cast(StyledCellType, data)

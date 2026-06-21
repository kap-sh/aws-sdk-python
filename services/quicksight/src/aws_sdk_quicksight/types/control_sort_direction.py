"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlSortDirection``."""

from typing import Literal, TypeAlias, cast

ControlSortDirection: TypeAlias = Literal[
    "ASC",
    "DESC",
    "USER_DEFINED_ORDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSortDirection) -> str:
    return value


def deserialize_json(data: str) -> ControlSortDirection:
    return cast(ControlSortDirection, data)

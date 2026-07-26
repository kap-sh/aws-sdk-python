"""Generated from Smithy shape ``com.amazonaws.datazone#FilterStatus``."""

from typing import Literal, TypeAlias, cast

FilterStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterStatus) -> str:
    return value


def deserialize_json(data: str) -> FilterStatus:
    return cast(FilterStatus, data)

"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeQuickSightQIndex``."""

from typing import Literal, TypeAlias, cast

IncludeQuickSightQIndex: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeQuickSightQIndex) -> str:
    return value


def deserialize_json(data: str) -> IncludeQuickSightQIndex:
    return cast(IncludeQuickSightQIndex, data)

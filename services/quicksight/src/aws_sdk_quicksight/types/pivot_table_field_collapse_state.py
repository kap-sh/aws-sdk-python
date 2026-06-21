"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseState``."""

from typing import Literal, TypeAlias, cast

PivotTableFieldCollapseState: TypeAlias = Literal[
    "COLLAPSED",
    "EXPANDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseState) -> str:
    return value


def deserialize_json(data: str) -> PivotTableFieldCollapseState:
    return cast(PivotTableFieldCollapseState, data)

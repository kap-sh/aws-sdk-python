"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardUIState``."""

from typing import Literal, TypeAlias, cast

DashboardUIState: TypeAlias = Literal[
    "EXPANDED",
    "COLLAPSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardUIState) -> str:
    return value


def deserialize_json(data: str) -> DashboardUIState:
    return cast(DashboardUIState, data)

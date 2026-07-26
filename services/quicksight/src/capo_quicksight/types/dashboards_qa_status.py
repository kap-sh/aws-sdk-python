"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardsQAStatus``."""

from typing import Literal, TypeAlias, cast

DashboardsQAStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardsQAStatus) -> str:
    return value


def deserialize_json(data: str) -> DashboardsQAStatus:
    return cast(DashboardsQAStatus, data)

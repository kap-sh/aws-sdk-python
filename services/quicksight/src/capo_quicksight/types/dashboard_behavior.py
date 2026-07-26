"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardBehavior``."""

from typing import Literal, TypeAlias, cast

DashboardBehavior: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardBehavior) -> str:
    return value


def deserialize_json(data: str) -> DashboardBehavior:
    return cast(DashboardBehavior, data)

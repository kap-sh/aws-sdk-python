"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardCustomizationStatus``."""

from typing import Literal, TypeAlias, cast

DashboardCustomizationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardCustomizationStatus) -> str:
    return value


def deserialize_json(data: str) -> DashboardCustomizationStatus:
    return cast(DashboardCustomizationStatus, data)

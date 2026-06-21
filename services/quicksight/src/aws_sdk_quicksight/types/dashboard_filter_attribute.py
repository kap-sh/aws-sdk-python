"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardFilterAttribute``."""

from typing import Literal, TypeAlias, cast

DashboardFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DASHBOARD_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DashboardFilterAttribute:
    return cast(DashboardFilterAttribute, data)

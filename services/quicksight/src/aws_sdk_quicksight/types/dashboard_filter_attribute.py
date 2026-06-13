"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "QUICKSIGHT_USER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DASHBOARD_NAME",
    )
)


def serialize_json(value: DashboardFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DashboardFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardFilterAttribute value: {data!r}")
    return cast(DashboardFilterAttribute, data)

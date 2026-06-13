"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardsQAStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DashboardsQAStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DashboardsQAStatus) -> str:
    return value


def deserialize_json(data: str) -> DashboardsQAStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardsQAStatus value: {data!r}")
    return cast(DashboardsQAStatus, data)

"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardCustomizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DashboardCustomizationStatus: TypeAlias = Literal[
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


def serialize_json(value: DashboardCustomizationStatus) -> str:
    return value


def deserialize_json(data: str) -> DashboardCustomizationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DashboardCustomizationStatus value: {data!r}"
        )
    return cast(DashboardCustomizationStatus, data)

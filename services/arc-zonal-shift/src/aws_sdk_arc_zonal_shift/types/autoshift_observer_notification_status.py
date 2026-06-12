"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftObserverNotificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

AutoshiftObserverNotificationStatus: TypeAlias = Literal[
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


def serialize_json(value: AutoshiftObserverNotificationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftObserverNotificationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutoshiftObserverNotificationStatus value: {data!r}"
        )
    return cast(AutoshiftObserverNotificationStatus, data)

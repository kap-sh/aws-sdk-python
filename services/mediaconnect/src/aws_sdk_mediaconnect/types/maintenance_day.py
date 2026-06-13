"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceDay``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MaintenanceDay: TypeAlias = Literal[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
)


def serialize_json(value: MaintenanceDay) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceDay:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceDay value: {data!r}")
    return cast(MaintenanceDay, data)

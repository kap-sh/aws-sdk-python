"""Generated from Smithy shape ``com.amazonaws.medialive#MaintenanceDay``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The currently selected maintenance day."""
MaintenanceDay: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    )
)


def serialize_json(value: MaintenanceDay) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceDay:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceDay value: {data!r}")
    return cast(MaintenanceDay, data)

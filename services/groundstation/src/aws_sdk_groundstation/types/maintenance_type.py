"""Generated from Smithy shape ``com.amazonaws.groundstation#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

MaintenanceType: TypeAlias = Literal[
    "PLANNED",
    "UNPLANNED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLANNED",
        "UNPLANNED",
    )
)


def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceType value: {data!r}")
    return cast(MaintenanceType, data)

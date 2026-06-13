"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MaintenanceType: TypeAlias = Literal[
    "PREFERRED_DAY_TIME",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREFERRED_DAY_TIME",
        "DEFAULT",
    )
)


def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceType value: {data!r}")
    return cast(MaintenanceType, data)

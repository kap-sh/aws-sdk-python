"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MaintenanceScheduleType: TypeAlias = Literal["WINDOW",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WINDOW",))


def serialize_json(value: MaintenanceScheduleType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceScheduleType value: {data!r}")
    return cast(MaintenanceScheduleType, data)

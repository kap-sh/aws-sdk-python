"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#MaintenanceWindowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

MaintenanceWindowType: TypeAlias = Literal[
    "SYSTEM",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "CUSTOM",
    )
)


def serialize_json(value: MaintenanceWindowType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceWindowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceWindowType value: {data!r}")
    return cast(MaintenanceWindowType, data)

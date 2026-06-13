"""Generated from Smithy shape ``com.amazonaws.s3tables#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

MaintenanceStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_json(value: MaintenanceStatus) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceStatus value: {data!r}")
    return cast(MaintenanceStatus, data)

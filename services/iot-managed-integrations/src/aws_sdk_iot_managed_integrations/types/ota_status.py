"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

OtaStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "COMPLETED",
    "DELETION_IN_PROGRESS",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELED",
        "COMPLETED",
        "DELETION_IN_PROGRESS",
        "SCHEDULED",
    )
)


def serialize_json(value: OtaStatus) -> str:
    return value


def deserialize_json(data: str) -> OtaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtaStatus value: {data!r}")
    return cast(OtaStatus, data)

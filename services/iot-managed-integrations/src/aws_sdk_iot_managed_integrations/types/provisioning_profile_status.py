"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ProvisioningProfileStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "CREATED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "CREATED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: ProvisioningProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisioningProfileStatus value: {data!r}")
    return cast(ProvisioningProfileStatus, data)

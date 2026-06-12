"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ProvisioningStatus: TypeAlias = Literal[
    "UNASSOCIATED",
    "PRE_ASSOCIATED",
    "DISCOVERED",
    "ACTIVATED",
    "DELETION_FAILED",
    "DELETE_IN_PROGRESS",
    "ISOLATED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNASSOCIATED",
        "PRE_ASSOCIATED",
        "DISCOVERED",
        "ACTIVATED",
        "DELETION_FAILED",
        "DELETE_IN_PROGRESS",
        "ISOLATED",
        "DELETED",
    )
)


def serialize_json(value: ProvisioningStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisioningStatus value: {data!r}")
    return cast(ProvisioningStatus, data)

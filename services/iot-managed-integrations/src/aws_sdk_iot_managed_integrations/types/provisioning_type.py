"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ProvisioningType: TypeAlias = Literal[
    "FLEET_PROVISIONING",
    "JITR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLEET_PROVISIONING",
        "JITR",
    )
)


def serialize_json(value: ProvisioningType) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisioningType value: {data!r}")
    return cast(ProvisioningType, data)

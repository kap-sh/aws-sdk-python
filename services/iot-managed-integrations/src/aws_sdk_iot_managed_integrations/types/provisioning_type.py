"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningType``."""

from typing import Literal, TypeAlias, cast

ProvisioningType: TypeAlias = Literal[
    "FLEET_PROVISIONING",
    "JITR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningType) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningType:
    return cast(ProvisioningType, data)

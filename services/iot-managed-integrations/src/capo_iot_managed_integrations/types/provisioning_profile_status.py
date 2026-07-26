"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningProfileStatus``."""

from typing import Literal, TypeAlias, cast

ProvisioningProfileStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "CREATED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningProfileStatus:
    return cast(ProvisioningProfileStatus, data)

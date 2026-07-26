"""Generated from Smithy shape ``com.amazonaws.appflow#PrivateConnectionProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

PrivateConnectionProvisioningStatus: TypeAlias = Literal[
    "FAILED",
    "PENDING",
    "CREATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionProvisioningStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionProvisioningStatus:
    return cast(PrivateConnectionProvisioningStatus, data)

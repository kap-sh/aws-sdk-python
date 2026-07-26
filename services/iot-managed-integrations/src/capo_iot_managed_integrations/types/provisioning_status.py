"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ProvisioningStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisioningStatus:
    return cast(ProvisioningStatus, data)

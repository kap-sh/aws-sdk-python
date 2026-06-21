"""Generated from Smithy shape ``com.amazonaws.appflow#PrivateConnectionProvisioningFailureCause``."""

from typing import Literal, TypeAlias, cast

PrivateConnectionProvisioningFailureCause: TypeAlias = Literal[
    "CONNECTOR_AUTHENTICATION",
    "CONNECTOR_SERVER",
    "INTERNAL_SERVER",
    "ACCESS_DENIED",
    "VALIDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionProvisioningFailureCause) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionProvisioningFailureCause:
    return cast(PrivateConnectionProvisioningFailureCause, data)

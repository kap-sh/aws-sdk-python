"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameStatus``."""

from typing import Literal, TypeAlias, cast

ServicePrincipalNameStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServicePrincipalNameStatus) -> str:
    return value


def deserialize_json(data: str) -> ServicePrincipalNameStatus:
    return cast(ServicePrincipalNameStatus, data)

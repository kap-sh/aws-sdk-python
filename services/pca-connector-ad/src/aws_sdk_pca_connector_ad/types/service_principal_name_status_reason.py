"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameStatusReason``."""

from typing import Literal, TypeAlias, cast

ServicePrincipalNameStatusReason: TypeAlias = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "SPN_EXISTS_ON_DIFFERENT_AD_OBJECT",
    "SPN_LIMIT_EXCEEDED",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServicePrincipalNameStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ServicePrincipalNameStatusReason:
    return cast(ServicePrincipalNameStatusReason, data)

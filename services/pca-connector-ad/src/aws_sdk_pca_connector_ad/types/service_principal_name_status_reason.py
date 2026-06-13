"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ServicePrincipalNameStatusReason: TypeAlias = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "SPN_EXISTS_ON_DIFFERENT_AD_OBJECT",
    "SPN_LIMIT_EXCEEDED",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECTORY_ACCESS_DENIED",
        "DIRECTORY_NOT_REACHABLE",
        "DIRECTORY_RESOURCE_NOT_FOUND",
        "SPN_EXISTS_ON_DIFFERENT_AD_OBJECT",
        "SPN_LIMIT_EXCEEDED",
        "INTERNAL_FAILURE",
    )
)


def serialize_json(value: ServicePrincipalNameStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ServicePrincipalNameStatusReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServicePrincipalNameStatusReason value: {data!r}"
        )
    return cast(ServicePrincipalNameStatusReason, data)

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ServicePrincipalNameStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: ServicePrincipalNameStatus) -> str:
    return value


def deserialize_json(data: str) -> ServicePrincipalNameStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServicePrincipalNameStatus value: {data!r}"
        )
    return cast(ServicePrincipalNameStatus, data)

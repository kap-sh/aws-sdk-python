"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ConnectorStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ConnectorStatusReason: TypeAlias = Literal[
    "CA_CERTIFICATE_REGISTRATION_FAILED",
    "DIRECTORY_ACCESS_DENIED",
    "INTERNAL_FAILURE",
    "INSUFFICIENT_FREE_ADDRESSES",
    "INVALID_SUBNET_IP_PROTOCOL",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_RESOURCE_NOT_FOUND",
    "SECURITY_GROUP_NOT_IN_VPC",
    "VPC_ACCESS_DENIED",
    "VPC_ENDPOINT_LIMIT_EXCEEDED",
    "VPC_RESOURCE_NOT_FOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CA_CERTIFICATE_REGISTRATION_FAILED",
        "DIRECTORY_ACCESS_DENIED",
        "INTERNAL_FAILURE",
        "INSUFFICIENT_FREE_ADDRESSES",
        "INVALID_SUBNET_IP_PROTOCOL",
        "PRIVATECA_ACCESS_DENIED",
        "PRIVATECA_RESOURCE_NOT_FOUND",
        "SECURITY_GROUP_NOT_IN_VPC",
        "VPC_ACCESS_DENIED",
        "VPC_ENDPOINT_LIMIT_EXCEEDED",
        "VPC_RESOURCE_NOT_FOUND",
    )
)


def serialize_json(value: ConnectorStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorStatusReason value: {data!r}")
    return cast(ConnectorStatusReason, data)

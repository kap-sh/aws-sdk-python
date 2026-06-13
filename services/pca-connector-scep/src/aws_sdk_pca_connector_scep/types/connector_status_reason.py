"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_scep.errors import DeserializationError

ConnectorStatusReason: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_INVALID_STATE",
    "PRIVATECA_RESOURCE_NOT_FOUND",
    "VPC_ENDPOINT_RESOURCE_NOT_FOUND",
    "VPC_ENDPOINT_DNS_ENTRIES_NOT_FOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_FAILURE",
        "PRIVATECA_ACCESS_DENIED",
        "PRIVATECA_INVALID_STATE",
        "PRIVATECA_RESOURCE_NOT_FOUND",
        "VPC_ENDPOINT_RESOURCE_NOT_FOUND",
        "VPC_ENDPOINT_DNS_ENTRIES_NOT_FOUND",
    )
)


def serialize_json(value: ConnectorStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorStatusReason value: {data!r}")
    return cast(ConnectorStatusReason, data)

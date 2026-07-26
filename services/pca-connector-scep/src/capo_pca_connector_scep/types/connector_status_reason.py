"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorStatusReason``."""

from typing import Literal, TypeAlias, cast

ConnectorStatusReason: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_INVALID_STATE",
    "PRIVATECA_RESOURCE_NOT_FOUND",
    "VPC_ENDPOINT_RESOURCE_NOT_FOUND",
    "VPC_ENDPOINT_DNS_ENTRIES_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatusReason:
    return cast(ConnectorStatusReason, data)

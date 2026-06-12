"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

AttachmentErrorCode: TypeAlias = Literal[
    "VPC_NOT_FOUND",
    "SUBNET_NOT_FOUND",
    "SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE",
    "SUBNET_NO_FREE_ADDRESSES",
    "SUBNET_UNSUPPORTED_AVAILABILITY_ZONE",
    "SUBNET_NO_IPV6_CIDRS",
    "VPN_CONNECTION_NOT_FOUND",
    "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED",
    "DIRECT_CONNECT_GATEWAY_NOT_FOUND",
    "DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS",
    "DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF",
    "VPN_EXISTING_ASSOCIATIONS",
    "VPC_UNSUPPORTED_FEATURES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VPC_NOT_FOUND",
        "SUBNET_NOT_FOUND",
        "SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE",
        "SUBNET_NO_FREE_ADDRESSES",
        "SUBNET_UNSUPPORTED_AVAILABILITY_ZONE",
        "SUBNET_NO_IPV6_CIDRS",
        "VPN_CONNECTION_NOT_FOUND",
        "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED",
        "DIRECT_CONNECT_GATEWAY_NOT_FOUND",
        "DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS",
        "DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF",
        "VPN_EXISTING_ASSOCIATIONS",
        "VPC_UNSUPPORTED_FEATURES",
    )
)


def serialize_json(value: AttachmentErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AttachmentErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentErrorCode value: {data!r}")
    return cast(AttachmentErrorCode, data)

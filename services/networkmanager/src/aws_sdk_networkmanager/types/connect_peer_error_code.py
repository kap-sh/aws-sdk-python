"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ConnectPeerErrorCode: TypeAlias = Literal[
    "EDGE_LOCATION_NO_FREE_IPS",
    "EDGE_LOCATION_PEER_DUPLICATE",
    "SUBNET_NOT_FOUND",
    "IP_OUTSIDE_SUBNET_CIDR_RANGE",
    "INVALID_INSIDE_CIDR_BLOCK",
    "NO_ASSOCIATED_CIDR_BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EDGE_LOCATION_NO_FREE_IPS",
        "EDGE_LOCATION_PEER_DUPLICATE",
        "SUBNET_NOT_FOUND",
        "IP_OUTSIDE_SUBNET_CIDR_RANGE",
        "INVALID_INSIDE_CIDR_BLOCK",
        "NO_ASSOCIATED_CIDR_BLOCK",
    )
)


def serialize_json(value: ConnectPeerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectPeerErrorCode value: {data!r}")
    return cast(ConnectPeerErrorCode, data)

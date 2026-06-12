"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

AttachmentType: TypeAlias = Literal[
    "CONNECT",
    "SITE_TO_SITE_VPN",
    "VPC",
    "DIRECT_CONNECT_GATEWAY",
    "TRANSIT_GATEWAY_ROUTE_TABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECT",
        "SITE_TO_SITE_VPN",
        "VPC",
        "DIRECT_CONNECT_GATEWAY",
        "TRANSIT_GATEWAY_ROUTE_TABLE",
    )
)


def serialize_json(value: AttachmentType) -> str:
    return value


def deserialize_json(data: str) -> AttachmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentType value: {data!r}")
    return cast(AttachmentType, data)

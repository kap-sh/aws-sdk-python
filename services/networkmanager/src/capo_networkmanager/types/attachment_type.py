"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentType``."""

from typing import Literal, TypeAlias, cast

AttachmentType: TypeAlias = Literal[
    "CONNECT",
    "SITE_TO_SITE_VPN",
    "VPC",
    "DIRECT_CONNECT_GATEWAY",
    "TRANSIT_GATEWAY_ROUTE_TABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentType) -> str:
    return value


def deserialize_json(data: str) -> AttachmentType:
    return cast(AttachmentType, data)

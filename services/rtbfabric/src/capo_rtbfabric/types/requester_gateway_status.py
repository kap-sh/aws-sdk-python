"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RequesterGatewayStatus``."""

from typing import Literal, TypeAlias, cast

RequesterGatewayStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "ACTIVE",
    "PENDING_DELETION",
    "DELETED",
    "ERROR",
    "PENDING_UPDATE",
    "ISOLATED",
    "PENDING_ISOLATION",
    "PENDING_RESTORATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequesterGatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> RequesterGatewayStatus:
    return cast(RequesterGatewayStatus, data)

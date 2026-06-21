"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderGatewayStatus``."""

from typing import Literal, TypeAlias, cast

ResponderGatewayStatus: TypeAlias = Literal[
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
def serialize_json(value: ResponderGatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> ResponderGatewayStatus:
    return cast(ResponderGatewayStatus, data)

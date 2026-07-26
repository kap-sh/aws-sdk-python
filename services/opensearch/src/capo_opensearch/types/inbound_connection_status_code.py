"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

InboundConnectionStatusCode: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "APPROVED",
    "PROVISIONING",
    "ACTIVE",
    "REJECTING",
    "REJECTED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> InboundConnectionStatusCode:
    return cast(InboundConnectionStatusCode, data)

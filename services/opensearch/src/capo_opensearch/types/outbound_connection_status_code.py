"""Generated from Smithy shape ``com.amazonaws.opensearch#OutboundConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

OutboundConnectionStatusCode: TypeAlias = Literal[
    "VALIDATING",
    "VALIDATION_FAILED",
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
def serialize_json(value: OutboundConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> OutboundConnectionStatusCode:
    return cast(OutboundConnectionStatusCode, data)

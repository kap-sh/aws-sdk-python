"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OutboundCrossClusterSearchConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

OutboundCrossClusterSearchConnectionStatusCode: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "VALIDATING",
    "VALIDATION_FAILED",
    "PROVISIONING",
    "ACTIVE",
    "REJECTED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundCrossClusterSearchConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> OutboundCrossClusterSearchConnectionStatusCode:
    return cast(OutboundCrossClusterSearchConnectionStatusCode, data)

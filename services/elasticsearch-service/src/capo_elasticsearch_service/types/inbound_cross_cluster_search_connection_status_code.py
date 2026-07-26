"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InboundCrossClusterSearchConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

InboundCrossClusterSearchConnectionStatusCode: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "APPROVED",
    "REJECTING",
    "REJECTED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundCrossClusterSearchConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> InboundCrossClusterSearchConnectionStatusCode:
    return cast(InboundCrossClusterSearchConnectionStatusCode, data)

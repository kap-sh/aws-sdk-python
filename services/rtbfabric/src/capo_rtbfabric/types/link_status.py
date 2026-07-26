"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkStatus``."""

from typing import Literal, TypeAlias, cast

LinkStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "PENDING_REQUEST",
    "REQUESTED",
    "ACCEPTED",
    "ACTIVE",
    "REJECTED",
    "FAILED",
    "PENDING_DELETION",
    "DELETED",
    "PENDING_UPDATE",
    "PENDING_ISOLATION",
    "ISOLATED",
    "PENDING_RESTORATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkStatus) -> str:
    return value


def deserialize_json(data: str) -> LinkStatus:
    return cast(LinkStatus, data)

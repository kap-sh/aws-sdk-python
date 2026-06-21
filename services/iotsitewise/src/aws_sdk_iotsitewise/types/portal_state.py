"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalState``."""

from typing import Literal, TypeAlias, cast

PortalState: TypeAlias = Literal[
    "CREATING",
    "PENDING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PortalState) -> str:
    return value


def deserialize_json(data: str) -> PortalState:
    return cast(PortalState, data)

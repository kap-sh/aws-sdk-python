"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityStatus``."""

from typing import Literal, TypeAlias, cast

CapabilityStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "DELETING",
    "DELETE_FAILED",
    "ACTIVE",
    "DEGRADED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> CapabilityStatus:
    return cast(CapabilityStatus, data)

"""Generated from Smithy shape ``com.amazonaws.eks#AddonStatus``."""

from typing import Literal, TypeAlias, cast

AddonStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "UPDATING",
    "DELETING",
    "DELETE_FAILED",
    "DEGRADED",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonStatus) -> str:
    return value


def deserialize_json(data: str) -> AddonStatus:
    return cast(AddonStatus, data)

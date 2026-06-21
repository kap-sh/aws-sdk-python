"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroupStatus``."""

from typing import Literal, TypeAlias, cast

KxScalingGroupStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxScalingGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> KxScalingGroupStatus:
    return cast(KxScalingGroupStatus, data)

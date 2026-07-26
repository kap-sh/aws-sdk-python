"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileStatus``."""

from typing import Literal, TypeAlias, cast

FargateProfileStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> FargateProfileStatus:
    return cast(FargateProfileStatus, data)

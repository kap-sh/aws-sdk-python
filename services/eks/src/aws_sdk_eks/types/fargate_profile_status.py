"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

FargateProfileStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "CREATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: FargateProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> FargateProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FargateProfileStatus value: {data!r}")
    return cast(FargateProfileStatus, data)

"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxScalingGroupStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETING",
        "DELETED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: KxScalingGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> KxScalingGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxScalingGroupStatus value: {data!r}")
    return cast(KxScalingGroupStatus, data)

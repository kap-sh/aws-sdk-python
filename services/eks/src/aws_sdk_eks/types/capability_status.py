"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "UPDATING",
        "DELETING",
        "DELETE_FAILED",
        "ACTIVE",
        "DEGRADED",
    )
)


def serialize_json(value: CapabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> CapabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityStatus value: {data!r}")
    return cast(CapabilityStatus, data)

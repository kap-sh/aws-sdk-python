"""Generated from Smithy shape ``com.amazonaws.eks#AddonStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "CREATE_FAILED",
        "UPDATING",
        "DELETING",
        "DELETE_FAILED",
        "DEGRADED",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: AddonStatus) -> str:
    return value


def deserialize_json(data: str) -> AddonStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddonStatus value: {data!r}")
    return cast(AddonStatus, data)

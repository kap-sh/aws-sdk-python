"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxClusterStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "CREATE_FAILED",
    "RUNNING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CREATING",
        "CREATE_FAILED",
        "RUNNING",
        "UPDATING",
        "DELETING",
        "DELETED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: KxClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> KxClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxClusterStatus value: {data!r}")
    return cast(KxClusterStatus, data)

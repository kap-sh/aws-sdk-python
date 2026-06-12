"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

NetworkStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATE_FAILED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "CREATE_FAILED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: NetworkStatus) -> str:
    return value


def deserialize_json(data: str) -> NetworkStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkStatus value: {data!r}")
    return cast(NetworkStatus, data)

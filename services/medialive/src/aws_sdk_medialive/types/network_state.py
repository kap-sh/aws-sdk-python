"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in DescribeNetworkResult, DescribeNetworkSummary, UpdateNetworkResult."""
NetworkState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "IDLE",
    "IN_USE",
    "UPDATING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETING",
        "IDLE",
        "IN_USE",
        "UPDATING",
        "DELETE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: NetworkState) -> str:
    return value


def deserialize_json(data: str) -> NetworkState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkState value: {data!r}")
    return cast(NetworkState, data)

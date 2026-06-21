"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NetworkState) -> str:
    return value


def deserialize_json(data: str) -> NetworkState:
    return cast(NetworkState, data)

"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in DescribeClusterSummary, DescribeClusterResult, UpdateClusterResult."""
ClusterState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
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
        "DELETE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: ClusterState) -> str:
    return value


def deserialize_json(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)

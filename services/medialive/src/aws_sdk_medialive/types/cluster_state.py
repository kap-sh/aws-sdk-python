"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ClusterState) -> str:
    return value


def deserialize_json(data: str) -> ClusterState:
    return cast(ClusterState, data)

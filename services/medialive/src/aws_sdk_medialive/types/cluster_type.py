"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterType``."""

from typing import Literal, TypeAlias, cast

"""Used in CreateClusterSummary, DescribeClusterSummary, DescribeClusterResult, UpdateClusterResult."""
ClusterType: TypeAlias = Literal["ON_PREMISES",]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterType) -> str:
    return value


def deserialize_json(data: str) -> ClusterType:
    return cast(ClusterType, data)

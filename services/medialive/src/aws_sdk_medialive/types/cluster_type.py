"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in CreateClusterSummary, DescribeClusterSummary, DescribeClusterResult, UpdateClusterResult."""
ClusterType: TypeAlias = Literal["ON_PREMISES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ON_PREMISES",))


def serialize_json(value: ClusterType) -> str:
    return value


def deserialize_json(data: str) -> ClusterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterType value: {data!r}")
    return cast(ClusterType, data)

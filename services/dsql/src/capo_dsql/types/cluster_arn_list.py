"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dsql.types.cluster_arn

ClusterArnList: TypeAlias = list["capo_dsql.types.cluster_arn.ClusterArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ClusterArnList:
    return list(data)

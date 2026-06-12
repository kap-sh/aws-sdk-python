"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_summary

ClusterList: TypeAlias = list["aws_sdk_dsql.types.cluster_summary.ClusterSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterList) -> list:
    import aws_sdk_dsql.types.cluster_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_dsql.types.cluster_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterList:
    import aws_sdk_dsql.types.cluster_summary
    out: ClusterList = []
    for item in data:
        out.append(aws_sdk_dsql.types.cluster_summary.deserialize_json(item))
    return out
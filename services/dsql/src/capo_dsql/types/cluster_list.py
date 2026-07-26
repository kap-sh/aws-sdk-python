"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dsql.types.cluster_summary

ClusterList: TypeAlias = list["capo_dsql.types.cluster_summary.ClusterSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterList) -> list:
    import capo_dsql.types.cluster_summary

    out: list = []
    for item in value:
        out.append(capo_dsql.types.cluster_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterList:
    import capo_dsql.types.cluster_summary

    out: ClusterList = []
    for item in data:
        out.append(capo_dsql.types.cluster_summary.deserialize_json(item))
    return out

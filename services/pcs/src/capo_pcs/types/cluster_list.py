"""Generated from Smithy shape ``com.amazonaws.pcs#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.cluster_summary

ClusterList: TypeAlias = list["capo_pcs.types.cluster_summary.ClusterSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterList) -> list:
    import capo_pcs.types.cluster_summary

    out: list = []
    for item in value:
        out.append(capo_pcs.types.cluster_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ClusterList:
    import capo_pcs.types.cluster_summary

    out: ClusterList = []
    for item in data:
        out.append(capo_pcs.types.cluster_summary.deserialize_aws_json_1_0(item))
    return out

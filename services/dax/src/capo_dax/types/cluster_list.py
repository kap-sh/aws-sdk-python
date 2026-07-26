"""Generated from Smithy shape ``com.amazonaws.dax#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.cluster

ClusterList: TypeAlias = list["capo_dax.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterList) -> list:
    import capo_dax.types.cluster

    out: list = []
    for item in value:
        out.append(capo_dax.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterList:
    import capo_dax.types.cluster

    out: ClusterList = []
    for item in data:
        out.append(capo_dax.types.cluster.deserialize_aws_json_1_1(item))
    return out

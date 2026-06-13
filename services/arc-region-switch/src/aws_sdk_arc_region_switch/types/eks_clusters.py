"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.eks_cluster

EksClusters: TypeAlias = list["aws_sdk_arc_region_switch.types.eks_cluster.EksCluster"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksClusters) -> list:
    import aws_sdk_arc_region_switch.types.eks_cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.eks_cluster.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EksClusters:
    import aws_sdk_arc_region_switch.types.eks_cluster

    out: EksClusters = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.eks_cluster.deserialize_aws_json_1_0(item)
        )
    return out

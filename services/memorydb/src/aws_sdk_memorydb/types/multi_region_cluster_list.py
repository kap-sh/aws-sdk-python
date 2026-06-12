"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.multi_region_cluster

MultiRegionClusterList: TypeAlias = list[
    "aws_sdk_memorydb.types.multi_region_cluster.MultiRegionCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionClusterList) -> list:
    import aws_sdk_memorydb.types.multi_region_cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_memorydb.types.multi_region_cluster.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MultiRegionClusterList:
    import aws_sdk_memorydb.types.multi_region_cluster

    out: MultiRegionClusterList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.multi_region_cluster.deserialize_aws_json_1_1(item)
        )
    return out

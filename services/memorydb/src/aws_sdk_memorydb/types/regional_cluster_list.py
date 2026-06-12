"""Generated from Smithy shape ``com.amazonaws.memorydb#RegionalClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.regional_cluster

RegionalClusterList: TypeAlias = list[
    "aws_sdk_memorydb.types.regional_cluster.RegionalCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionalClusterList) -> list:
    import aws_sdk_memorydb.types.regional_cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.regional_cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegionalClusterList:
    import aws_sdk_memorydb.types.regional_cluster

    out: RegionalClusterList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.regional_cluster.deserialize_aws_json_1_1(item)
        )
    return out

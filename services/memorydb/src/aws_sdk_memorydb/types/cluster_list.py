"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster

ClusterList: TypeAlias = list["aws_sdk_memorydb.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterList) -> list:
    import aws_sdk_memorydb.types.cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterList:
    import aws_sdk_memorydb.types.cluster

    out: ClusterList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.cluster.deserialize_aws_json_1_1(item))
    return out

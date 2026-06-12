"""Generated from Smithy shape ``com.amazonaws.memorydb#UnprocessedClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.unprocessed_cluster

UnprocessedClusterList: TypeAlias = list[
    "aws_sdk_memorydb.types.unprocessed_cluster.UnprocessedCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedClusterList) -> list:
    import aws_sdk_memorydb.types.unprocessed_cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_memorydb.types.unprocessed_cluster.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedClusterList:
    import aws_sdk_memorydb.types.unprocessed_cluster

    out: UnprocessedClusterList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.unprocessed_cluster.deserialize_aws_json_1_1(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.memorydb#UnprocessedClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.unprocessed_cluster

UnprocessedClusterList: TypeAlias = list[
    "capo_memorydb.types.unprocessed_cluster.UnprocessedCluster"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedClusterList) -> list:
    import capo_memorydb.types.unprocessed_cluster

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.unprocessed_cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedClusterList:
    import capo_memorydb.types.unprocessed_cluster

    out: UnprocessedClusterList = []
    for item in data:
        out.append(
            capo_memorydb.types.unprocessed_cluster.deserialize_aws_json_1_1(item)
        )
    return out

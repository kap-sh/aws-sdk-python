"""Generated from Smithy shape ``com.amazonaws.keyspaces#ClusteringKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.clustering_key

ClusteringKeyList: TypeAlias = list[
    "aws_sdk_keyspaces.types.clustering_key.ClusteringKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusteringKeyList) -> list:
    import aws_sdk_keyspaces.types.clustering_key

    out: list = []
    for item in value:
        out.append(aws_sdk_keyspaces.types.clustering_key.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ClusteringKeyList:
    import aws_sdk_keyspaces.types.clustering_key

    out: ClusteringKeyList = []
    for item in data:
        out.append(
            aws_sdk_keyspaces.types.clustering_key.deserialize_aws_json_1_0(item)
        )
    return out

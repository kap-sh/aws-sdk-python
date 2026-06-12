"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfClusterInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster_info

__listOfClusterInfo: TypeAlias = list["aws_sdk_kafka.types.cluster_info.ClusterInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterInfo) -> list:
    import aws_sdk_kafka.types.cluster_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.cluster_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClusterInfo:
    import aws_sdk_kafka.types.cluster_info

    out: __listOfClusterInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.cluster_info.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfClusterOperationInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster_operation_info

__listOfClusterOperationInfo: TypeAlias = list[
    "aws_sdk_kafka.types.cluster_operation_info.ClusterOperationInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterOperationInfo) -> list:
    import aws_sdk_kafka.types.cluster_operation_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.cluster_operation_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClusterOperationInfo:
    import aws_sdk_kafka.types.cluster_operation_info

    out: __listOfClusterOperationInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.cluster_operation_info.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfClusterOperationV2Summary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster_operation_v2_summary

__listOfClusterOperationV2Summary: TypeAlias = list[
    "aws_sdk_kafka.types.cluster_operation_v2_summary.ClusterOperationV2Summary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterOperationV2Summary) -> list:
    import aws_sdk_kafka.types.cluster_operation_v2_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kafka.types.cluster_operation_v2_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfClusterOperationV2Summary:
    import aws_sdk_kafka.types.cluster_operation_v2_summary

    out: __listOfClusterOperationV2Summary = []
    for item in data:
        out.append(
            aws_sdk_kafka.types.cluster_operation_v2_summary.deserialize_json(item)
        )
    return out

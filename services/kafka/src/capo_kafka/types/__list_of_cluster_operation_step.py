"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfClusterOperationStep``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.cluster_operation_step

__listOfClusterOperationStep: TypeAlias = list[
    "capo_kafka.types.cluster_operation_step.ClusterOperationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterOperationStep) -> list:
    import capo_kafka.types.cluster_operation_step

    out: list = []
    for item in value:
        out.append(capo_kafka.types.cluster_operation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClusterOperationStep:
    import capo_kafka.types.cluster_operation_step

    out: __listOfClusterOperationStep = []
    for item in data:
        out.append(capo_kafka.types.cluster_operation_step.deserialize_json(item))
    return out

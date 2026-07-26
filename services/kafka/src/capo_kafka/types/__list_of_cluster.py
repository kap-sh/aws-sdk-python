"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfCluster``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.cluster

__listOfCluster: TypeAlias = list["capo_kafka.types.cluster.Cluster"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCluster) -> list:
    import capo_kafka.types.cluster

    out: list = []
    for item in value:
        out.append(capo_kafka.types.cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCluster:
    import capo_kafka.types.cluster

    out: __listOfCluster = []
    for item in data:
        out.append(capo_kafka.types.cluster.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#Clusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.cluster

Clusters: TypeAlias = list["capo_ecs.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Clusters) -> list:
    import capo_ecs.types.cluster

    out: list = []
    for item in value:
        out.append(capo_ecs.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Clusters:
    import capo_ecs.types.cluster

    out: Clusters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.cluster.deserialize_aws_json_1_1(item))
    return out

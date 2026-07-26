"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.cluster_field

ClusterFieldList: TypeAlias = list["capo_ecs.types.cluster_field.ClusterField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterFieldList) -> list:
    import capo_ecs.types.cluster_field

    out: list = []
    for item in value:
        out.append(capo_ecs.types.cluster_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterFieldList:
    import capo_ecs.types.cluster_field

    out: ClusterFieldList = []
    for item in data:
        out.append(capo_ecs.types.cluster_field.deserialize_aws_json_1_1(item))
    return out

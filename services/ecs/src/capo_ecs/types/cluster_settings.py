"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.cluster_setting

ClusterSettings: TypeAlias = list["capo_ecs.types.cluster_setting.ClusterSetting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSettings) -> list:
    import capo_ecs.types.cluster_setting

    out: list = []
    for item in value:
        out.append(capo_ecs.types.cluster_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterSettings:
    import capo_ecs.types.cluster_setting

    out: ClusterSettings = []
    for item in data:
        out.append(capo_ecs.types.cluster_setting.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster_setting

ClusterSettings: TypeAlias = list["aws_sdk_ecs.types.cluster_setting.ClusterSetting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSettings) -> list:
    import aws_sdk_ecs.types.cluster_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.cluster_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterSettings:
    import aws_sdk_ecs.types.cluster_setting

    out: ClusterSettings = []
    for item in data:
        out.append(aws_sdk_ecs.types.cluster_setting.deserialize_aws_json_1_1(item))
    return out

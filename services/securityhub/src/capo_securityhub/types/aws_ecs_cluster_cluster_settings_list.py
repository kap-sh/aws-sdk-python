"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterClusterSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_cluster_cluster_settings_details

AwsEcsClusterClusterSettingsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_cluster_cluster_settings_details.AwsEcsClusterClusterSettingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterClusterSettingsList) -> list:
    import capo_securityhub.types.aws_ecs_cluster_cluster_settings_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_cluster_cluster_settings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsClusterClusterSettingsList:
    import capo_securityhub.types.aws_ecs_cluster_cluster_settings_details

    out: AwsEcsClusterClusterSettingsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_cluster_cluster_settings_details.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList: TypeAlias = list[
    "capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList,
) -> list:
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList:
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

    out: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.deserialize_json(
                item
            )
        )
    return out

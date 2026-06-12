"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList,
) -> list:
    import aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList:
    import aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details

    out: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_details.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataBlockDeviceMappingSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details

AwsEc2LaunchTemplateDataBlockDeviceMappingSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataBlockDeviceMappingSetList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2LaunchTemplateDataBlockDeviceMappingSetList:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details

    out: AwsEc2LaunchTemplateDataBlockDeviceMappingSetList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_details.deserialize_json(
                item
            )
        )
    return out

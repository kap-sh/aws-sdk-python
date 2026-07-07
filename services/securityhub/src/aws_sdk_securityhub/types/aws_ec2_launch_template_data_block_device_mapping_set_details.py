"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails(TypedDict, closed=True):
    device_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The device name. </p>"""
    ebs: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details.AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails"
    ]
    """<p> Parameters used to automatically set up Amazon EBS volumes when the instance is launched. </p>"""
    no_device: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Omits the device from the block device mapping when an empty string is specified. </p>"""
    virtual_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for <code>ephemeral0</code> and <code>ephemeral1</code>. The number of available instance store volumes depends on the instance type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "ebs" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details

        out["Ebs"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details.serialize_json(
                value["ebs"]
            )
        )
    if "no_device" in value:
        out["NoDevice"] = value["no_device"]
    if "virtual_name" in value:
        out["VirtualName"] = value["virtual_name"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails:
    out: AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Ebs" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details

        out["ebs"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_ebs_details.deserialize_json(
                data["Ebs"]
            )
        )
    if "NoDevice" in data:
        out["no_device"] = data["NoDevice"]
    if "VirtualName" in data:
        out["virtual_name"] = data["VirtualName"]
    return out

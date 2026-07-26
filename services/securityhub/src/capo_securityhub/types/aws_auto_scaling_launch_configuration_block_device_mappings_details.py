"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails(
    TypedDict, closed=True
):
    device_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The device name that is exposed to the EC2 instance. For example, <code>/dev/sdh</code> or <code>xvdh</code>.</p>"""
    ebs: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails"
    ]
    """<p>Parameters that are used to automatically set up Amazon EBS volumes when an instance is launched.</p>"""
    no_device: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to suppress the device that is included in the block device mapping of the Amazon Machine Image (AMI).</p> <p>If <code>NoDevice</code> is <code>true</code>, then you cannot specify <code>Ebs</code>.></p>"""
    virtual_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the virtual device (for example, <code>ephemeral0</code>).</p> <p>You can provide either <code>VirtualName</code> or <code>Ebs</code>, but not both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails,
) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "ebs" in value:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details

        out["Ebs"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details.serialize_json(
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
) -> AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails:
    out: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Ebs" in data:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details

        out["ebs"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details.deserialize_json(
                data["Ebs"]
            )
        )
    if "NoDevice" in data:
        out["no_device"] = data["NoDevice"]
    if "VirtualName" in data:
        out["virtual_name"] = data["VirtualName"]
    return out

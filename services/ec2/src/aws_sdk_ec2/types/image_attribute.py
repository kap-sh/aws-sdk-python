"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.block_device_mapping_list
    import aws_sdk_ec2.types.launch_permission_list
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class ImageAttribute(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>A description for the AMI.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The kernel ID.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The RAM disk ID.</p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The boot mode.</p>"""
    tpm_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>If the image is configured for NitroTPM support, the value is <code>v2.0</code>.</p>"""
    uefi_data: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData\">GetInstanceUefiData</a> command. You can inspect and modify the UEFI data by using the <a href=\"https://github.com/awslabs/python-uefivars\">python-uefivars tool</a> on GitHub. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html\">UEFI Secure Boot for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    last_launched_time: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.</p> <note> <p> <code>lastLaunchedTime</code> data is available starting April 2017.</p> </note>"""
    imds_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>If <code>v2.0</code>, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    deregistration_protection: NotRequired[
        "aws_sdk_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Indicates whether deregistration protection is enabled for the AMI.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    launch_permissions: NotRequired[
        "aws_sdk_ec2.types.launch_permission_list.LaunchPermissionList"
    ]
    """<p>The launch permissions.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>The block device mapping entries.</p>"""

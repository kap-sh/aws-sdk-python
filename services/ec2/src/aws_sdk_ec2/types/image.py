"""Generated from Smithy shape ``com.amazonaws.ec2#Image``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_values
    import aws_sdk_ec2.types.block_device_mapping_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.device_type
    import aws_sdk_ec2.types.hypervisor_type
    import aws_sdk_ec2.types.image_state
    import aws_sdk_ec2.types.image_type_values
    import aws_sdk_ec2.types.imds_support_values
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.state_reason
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tpm_support_values
    import aws_sdk_ec2.types.virtualization_type


class Image(TypedDict):
    platform_details: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The platform details associated with the billing code of the AMI. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html\">Understand AMI billing information</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    usage_operation: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. <code>usageOperation</code> corresponds to the <a href=\"https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation\">lineitem/Operation</a> column on your Amazon Web Services Cost and Usage Report and in the <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html\">Amazon Web Services Price List API</a>. You can view these fields on the <b>Instances</b> or <b>AMIs</b> pages in the Amazon EC2 console, or in the responses that are returned by the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html\">DescribeImages</a> command in the Amazon EC2 API, or the <a href=\"https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html\">describe-images</a> command in the CLI.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>Any block device mapping entries.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AMI that was provided during image creation.</p>"""
    ena_support: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether enhanced networking with ENA is enabled.</p>"""
    hypervisor: NotRequired["aws_sdk_ec2.types.hypervisor_type.HypervisorType"]
    """<p>The hypervisor type of the image. Only <code>xen</code> is supported. <code>ovm</code> is not supported.</p>"""
    image_owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code>).</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AMI that was provided during image creation.</p>"""
    root_device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    root_device_type: NotRequired["aws_sdk_ec2.types.device_type.DeviceType"]
    """<p>The type of root device used by the AMI. The AMI can use an Amazon EBS volume or an instance store volume.</p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.state_reason.StateReason"]
    """<p>The reason for the state change.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the image.</p>"""
    virtualization_type: NotRequired[
        "aws_sdk_ec2.types.virtualization_type.VirtualizationType"
    ]
    """<p>The type of virtualization of the AMI.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the image. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html\">Instance launch behavior with Amazon EC2 boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    tpm_support: NotRequired["aws_sdk_ec2.types.tpm_support_values.TpmSupportValues"]
    """<p>If the image is configured for NitroTPM support, the value is <code>v2.0</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html\">NitroTPM</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    deprecation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time to deprecate the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z. If you specified a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.</p>"""
    imds_support: NotRequired["aws_sdk_ec2.types.imds_support_values.ImdsSupportValues"]
    """<p>If <code>v2.0</code>, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    source_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance that the AMI was created from if the AMI was created using <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html\">CreateImage</a>. This field only appears if the AMI was created using CreateImage.</p>"""
    deregistration_protection: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates whether deregistration protection is enabled for the AMI.</p>"""
    last_launched_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.</p> <note> <p> <code>lastLaunchedTime</code> data is available starting April 2017.</p> </note>"""
    image_allowed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If <code>false</code> and Allowed AMIs is set to <code>enabled</code>, the AMI can't be discovered or used in the account. If <code>false</code> and Allowed AMIs is set to <code>audit-mode</code>, the AMI can be discovered and used in the account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html\">Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    source_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source AMI from which the AMI was created.</p>"""
    source_image_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the source AMI.</p>"""
    free_tier_eligible: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image is eligible for Amazon Web Services Free Tier.</p> <ul> <li> <p>If <code>true</code>, the AMI is eligible for Free Tier and can be used to launch instances under the Free Tier limits.</p> </li> <li> <p>If <code>false</code>, the AMI is not eligible for Free Tier.</p> </li> </ul>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    image_location: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The location of the AMI.</p>"""
    state: NotRequired["aws_sdk_ec2.types.image_state.ImageState"]
    """<p>The current state of the AMI. If the state is <code>available</code>, the image is successfully registered and can be used to launch an instance.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the image.</p>"""
    creation_date: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the image was created.</p>"""
    public: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image has public launch permissions. The value is <code>true</code> if this image has public launch permissions or <code>false</code> if it has only implicit and explicit launch permissions.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>Any product codes associated with the AMI.</p>"""
    architecture: NotRequired[
        "aws_sdk_ec2.types.architecture_values.ArchitectureValues"
    ]
    """<p>The architecture of the image.</p>"""
    image_type: NotRequired["aws_sdk_ec2.types.image_type_values.ImageTypeValues"]
    """<p>The type of image.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The kernel associated with the image, if any. Only applicable for machine images.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The RAM disk associated with the image, if any. Only applicable for machine images.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>This value is set to <code>windows</code> for Windows AMIs; otherwise, it is blank.</p>"""

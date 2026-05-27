"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_values
    import aws_sdk_ec2.types.billing_product_list
    import aws_sdk_ec2.types.block_device_mapping_request_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.image_description_request
    import aws_sdk_ec2.types.image_name_request
    import aws_sdk_ec2.types.image_uefi_data_request
    import aws_sdk_ec2.types.imds_support_values
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.tpm_support_values


class RegisterImageRequest(TypedDict):
    image_location: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The full path to your AMI manifest in Amazon S3 storage. The specified bucket must have the <code>aws-exec-read</code> canned access control list (ACL) to ensure that it can be accessed by Amazon EC2. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl\">Canned ACL</a> in the <i>Amazon S3 Service Developer Guide</i>.</p>"""
    billing_products: NotRequired[
        "aws_sdk_ec2.types.billing_product_list.BillingProductList"
    ]
    """<p>The billing product codes. Your account must be authorized to specify billing product codes.</p> <p>If your account is not authorized to specify billing product codes, you can publish AMIs that include billable software and list them on the Amazon Web Services Marketplace. You must first register as a seller on the Amazon Web Services Marketplace. For more information, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html\">Getting started as an Amazon Web Services Marketplace seller</a> and <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/ami-products.html\">AMI-based products in Amazon Web Services Marketplace</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the AMI. A value of <code>uefi-preferred</code> indicates that the AMI supports both UEFI and Legacy BIOS.</p> <note> <p>The operating system contained in the AMI must be configured to support the specified boot mode.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html\">Instance launch behavior with Amazon EC2 boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    tpm_support: NotRequired["aws_sdk_ec2.types.tpm_support_values.TpmSupportValues"]
    """<p>Set to <code>v2.0</code> to enable Trusted Platform Module (TPM) support. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html\">NitroTPM</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    uefi_data: NotRequired[
        "aws_sdk_ec2.types.image_uefi_data_request.ImageUefiDataRequest"
    ]
    """<p>Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData\">GetInstanceUefiData</a> command. You can inspect and modify the UEFI data by using the <a href=\"https://github.com/awslabs/python-uefivars\">python-uefivars tool</a> on GitHub. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html\">UEFI Secure Boot for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    imds_support: NotRequired["aws_sdk_ec2.types.imds_support_values.ImdsSupportValues"]
    """<p>Set to <code>v2.0</code> to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>If you set the value to <code>v2.0</code>, make sure that your AMI software can support IMDSv2.</p> </note>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the AMI.</p> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>. If you specify another value for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI after it has been registered, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    name: NotRequired["aws_sdk_ec2.types.image_name_request.ImageNameRequest"]
    """<p>A name for your AMI.</p> <p>Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)</p>"""
    description: NotRequired[
        "aws_sdk_ec2.types.image_description_request.ImageDescriptionRequest"
    ]
    """<p>A description for your AMI.</p>"""
    architecture: NotRequired[
        "aws_sdk_ec2.types.architecture_values.ArchitectureValues"
    ]
    """<p>The architecture of the AMI.</p> <p>Default: For Amazon EBS-backed AMIs, <code>i386</code>. For instance store-backed AMIs, the architecture specified in the manifest file.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p>"""
    root_device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
    ]
    """<p>The block device mapping entries.</p> <p>If you specify an Amazon EBS volume using the ID of an Amazon EBS snapshot, you can't specify the encryption state of the volume.</p> <p>If you create an AMI on an Outpost, then all backing snapshots must be on the same Outpost or in the Region of that Outpost. AMIs on an Outpost that include local snapshots can be used to launch instances on the same Outpost only. For more information, <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#ami\">Create AMIs from local snapshots</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    virtualization_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of virtualization (<code>hvm</code> | <code>paravirtual</code>).</p> <p>Default: <code>paravirtual</code> </p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Set to <code>simple</code> to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.</p> <p>There is no way to disable <code>sriovNetSupport</code> at this time.</p> <p>This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.</p>"""
    ena_support: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI.</p> <p>This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.</p>"""

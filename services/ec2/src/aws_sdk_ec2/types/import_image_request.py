"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.client_data
    import aws_sdk_ec2.types.image_disk_container_list
    import aws_sdk_ec2.types.import_image_license_specification_list_request
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class ImportImageRequest(TypedDict):
    architecture: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The architecture of the virtual machine.</p> <p>Valid values: <code>i386</code> | <code>x86_64</code> </p>"""
    client_data: NotRequired["aws_sdk_ec2.types.client_data.ClientData"]
    """<p>The client-specific data.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to enable idempotency for VM import requests.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description string for the import image task.</p>"""
    disk_containers: NotRequired[
        "aws_sdk_ec2.types.image_disk_container_list.ImageDiskContainerList"
    ]
    """<p>Information about the disk containers.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether the destination AMI of the imported image should be encrypted. The default KMS key for EBS is used unless you specify a non-default KMS key using <code>KmsKeyId</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html\">Amazon EBS Encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    hypervisor: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target hypervisor platform.</p> <p>Valid values: <code>xen</code> </p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>An identifier for the symmetric KMS key to use when creating the encrypted AMI. This parameter is only required if you want to use a non-default KMS key; if this parameter is not specified, the default KMS key for EBS is used. If a <code>KmsKeyId</code> is specified, the <code>Encrypted</code> flag must also be set. </p> <p>The KMS key identifier may be provided in any of the following formats: </p> <ul> <li> <p>Key ID</p> </li> <li> <p>Key alias</p> </li> <li> <p>ARN using key ID. The ID ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>key</code> namespace, and then the key ID. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:key/<i>abcd1234-a123-456a-a12b-a123b4cd56ef</i>.</p> </li> <li> <p>ARN using key alias. The alias ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>alias</code> namespace, and then the key alias. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:alias/<i>ExampleAlias</i>. </p> </li> </ul> <p>Amazon Web Services parses <code>KmsKeyId</code> asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure. </p> <p>The specified KMS key must exist in the Region that the AMI is being copied to.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    license_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The license type to be used for the Amazon Machine Image (AMI) after importing.</p> <p>Specify <code>AWS</code> to replace the source-system license with an Amazon Web Services license or <code>BYOL</code> to retain the source-system license. Leaving this parameter undefined is the same as choosing <code>AWS</code> when importing a Windows Server operating system, and the same as choosing <code>BYOL</code> when importing a Windows client operating system (such as Windows 10) or a Linux operating system.</p> <p>To use <code>BYOL</code>, you must have existing licenses with rights to use these licenses in a third party cloud, such as Amazon Web Services. For more information, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#prerequisites-image\">Prerequisites</a> in the VM Import/Export User Guide.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The operating system of the virtual machine. If you import a VM that is compatible with Unified Extensible Firmware Interface (UEFI) using an EBS snapshot, you must specify a value for the platform.</p> <p>Valid values: <code>Windows</code> | <code>Linux</code> </p>"""
    role_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the role to use when not using the default role, 'vmimport'.</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.import_image_license_specification_list_request.ImportImageLicenseSpecificationListRequest"
    ]
    """<p>The ARNs of the license configurations.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the import image task during creation.</p>"""
    usage_operation: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The usage operation value. For more information, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#prerequisites\">Licensing options</a> in the <i>VM Import/Export User Guide</i>.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the virtual machine.</p> <note> <p>The <code>uefi-preferred</code> boot mode isn't supported for importing images. For more information, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-boot-modes\">Boot modes</a> in the <i>VM Import/Export User Guide</i>.</p> </note>"""

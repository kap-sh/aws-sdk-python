"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_limit_type
    import aws_sdk_ec2.types.ebs_card_info_list
    import aws_sdk_ec2.types.ebs_encryption_support
    import aws_sdk_ec2.types.ebs_nvme_support
    import aws_sdk_ec2.types.ebs_optimized_info
    import aws_sdk_ec2.types.ebs_optimized_support
    import aws_sdk_ec2.types.maximum_ebs_attachments
    import aws_sdk_ec2.types.maximum_ebs_cards


class EbsInfo(TypedDict):
    ebs_optimized_support: NotRequired[
        "aws_sdk_ec2.types.ebs_optimized_support.EbsOptimizedSupport"
    ]
    """<p>Indicates whether the instance type is Amazon EBS-optimized. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html\">Amazon EBS-optimized instances</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    encryption_support: NotRequired[
        "aws_sdk_ec2.types.ebs_encryption_support.EbsEncryptionSupport"
    ]
    """<p>Indicates whether Amazon EBS encryption is supported.</p>"""
    ebs_optimized_info: NotRequired[
        "aws_sdk_ec2.types.ebs_optimized_info.EbsOptimizedInfo"
    ]
    """<p>Describes the optimized EBS performance for the instance type.</p>"""
    nvme_support: NotRequired["aws_sdk_ec2.types.ebs_nvme_support.EbsNvmeSupport"]
    """<p>Indicates whether non-volatile memory express (NVMe) is supported.</p>"""
    maximum_ebs_attachments: NotRequired[
        "aws_sdk_ec2.types.maximum_ebs_attachments.MaximumEbsAttachments"
    ]
    """<p>Indicates the maximum number of Amazon EBS volumes that can be attached to the instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html\">Amazon EBS volume limits for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    attachment_limit_type: NotRequired[
        "aws_sdk_ec2.types.attachment_limit_type.AttachmentLimitType"
    ]
    """<p>Indicates whether the instance type features a shared or dedicated Amazon EBS volume attachment limit. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html\">Amazon EBS volume limits for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    maximum_ebs_cards: NotRequired[
        "aws_sdk_ec2.types.maximum_ebs_cards.MaximumEbsCards"
    ]
    """<p>Indicates the number of EBS cards supported by the instance type.</p>"""
    ebs_cards: NotRequired["aws_sdk_ec2.types.ebs_card_info_list.EbsCardInfoList"]
    """<p>Describes the EBS cards available for the instance type.</p>"""

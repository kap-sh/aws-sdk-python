"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ebs_optimized_support" in value:
        import aws_sdk_ec2.types.ebs_optimized_support

        aws_sdk_ec2.types.ebs_optimized_support.serialize_ec2_query(
            value["ebs_optimized_support"], pairs, f"{prefix}.EbsOptimizedSupport"
        )
    if "encryption_support" in value:
        import aws_sdk_ec2.types.ebs_encryption_support

        aws_sdk_ec2.types.ebs_encryption_support.serialize_ec2_query(
            value["encryption_support"], pairs, f"{prefix}.EncryptionSupport"
        )
    if "ebs_optimized_info" in value:
        import aws_sdk_ec2.types.ebs_optimized_info

        aws_sdk_ec2.types.ebs_optimized_info.serialize_ec2_query(
            value["ebs_optimized_info"], pairs, f"{prefix}.EbsOptimizedInfo"
        )
    if "nvme_support" in value:
        import aws_sdk_ec2.types.ebs_nvme_support

        aws_sdk_ec2.types.ebs_nvme_support.serialize_ec2_query(
            value["nvme_support"], pairs, f"{prefix}.NvmeSupport"
        )
    if "maximum_ebs_attachments" in value:
        pairs.append(
            (f"{prefix}.MaximumEbsAttachments", str(value["maximum_ebs_attachments"]))
        )
    if "attachment_limit_type" in value:
        import aws_sdk_ec2.types.attachment_limit_type

        aws_sdk_ec2.types.attachment_limit_type.serialize_ec2_query(
            value["attachment_limit_type"], pairs, f"{prefix}.AttachmentLimitType"
        )
    if "maximum_ebs_cards" in value:
        pairs.append((f"{prefix}.MaximumEbsCards", str(value["maximum_ebs_cards"])))
    if "ebs_cards" in value:
        import aws_sdk_ec2.types.ebs_card_info_list

        aws_sdk_ec2.types.ebs_card_info_list.serialize_ec2_query(
            value["ebs_cards"], pairs, f"{prefix}.EbsCardSet"
        )


def deserialize_ec2_query(el: Element) -> EbsInfo:
    out: EbsInfo = {}  # type: ignore[typeddict-item]
    child_ebs_optimized_support = el.find("EbsOptimizedSupport")
    if child_ebs_optimized_support is not None:
        import aws_sdk_ec2.types.ebs_optimized_support

        out["ebs_optimized_support"] = (
            aws_sdk_ec2.types.ebs_optimized_support.deserialize_ec2_query(
                child_ebs_optimized_support
            )
        )
    child_encryption_support = el.find("EncryptionSupport")
    if child_encryption_support is not None:
        import aws_sdk_ec2.types.ebs_encryption_support

        out["encryption_support"] = (
            aws_sdk_ec2.types.ebs_encryption_support.deserialize_ec2_query(
                child_encryption_support
            )
        )
    child_ebs_optimized_info = el.find("EbsOptimizedInfo")
    if child_ebs_optimized_info is not None:
        import aws_sdk_ec2.types.ebs_optimized_info

        out["ebs_optimized_info"] = (
            aws_sdk_ec2.types.ebs_optimized_info.deserialize_ec2_query(
                child_ebs_optimized_info
            )
        )
    child_nvme_support = el.find("NvmeSupport")
    if child_nvme_support is not None:
        import aws_sdk_ec2.types.ebs_nvme_support

        out["nvme_support"] = aws_sdk_ec2.types.ebs_nvme_support.deserialize_ec2_query(
            child_nvme_support
        )
    child_maximum_ebs_attachments = el.find("MaximumEbsAttachments")
    if child_maximum_ebs_attachments is not None:
        out["maximum_ebs_attachments"] = int(child_maximum_ebs_attachments.text or "")
    child_attachment_limit_type = el.find("AttachmentLimitType")
    if child_attachment_limit_type is not None:
        import aws_sdk_ec2.types.attachment_limit_type

        out["attachment_limit_type"] = (
            aws_sdk_ec2.types.attachment_limit_type.deserialize_ec2_query(
                child_attachment_limit_type
            )
        )
    child_maximum_ebs_cards = el.find("MaximumEbsCards")
    if child_maximum_ebs_cards is not None:
        out["maximum_ebs_cards"] = int(child_maximum_ebs_cards.text or "")
    if el.find("EbsCardSet") is not None:
        import aws_sdk_ec2.types.ebs_card_info_list

        out["ebs_cards"] = aws_sdk_ec2.types.ebs_card_info_list.deserialize_ec2_query(
            el, "EbsCardSet"
        )
    return out

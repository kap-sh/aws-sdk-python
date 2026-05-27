"""Generated from Smithy shape ``com.amazonaws.ec2#EbsCardInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_card_info

EbsCardInfoList: TypeAlias = list["aws_sdk_ec2.types.ebs_card_info.EbsCardInfo"]

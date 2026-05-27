"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkCardInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_card_info

NetworkCardInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.network_card_info.NetworkCardInfo"
]

"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.additional_detail

AdditionalDetailList: TypeAlias = list[
    "aws_sdk_ec2.types.additional_detail.AdditionalDetail"
]

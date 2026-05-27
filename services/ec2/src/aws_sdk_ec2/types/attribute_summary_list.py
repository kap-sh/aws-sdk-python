"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_summary

AttributeSummaryList: TypeAlias = list[
    "aws_sdk_ec2.types.attribute_summary.AttributeSummary"
]

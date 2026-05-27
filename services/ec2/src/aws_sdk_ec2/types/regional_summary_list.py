"""Generated from Smithy shape ``com.amazonaws.ec2#RegionalSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.regional_summary

RegionalSummaryList: TypeAlias = list[
    "aws_sdk_ec2.types.regional_summary.RegionalSummary"
]

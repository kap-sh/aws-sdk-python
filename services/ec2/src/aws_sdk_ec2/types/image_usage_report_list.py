"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report

ImageUsageReportList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_report.ImageUsageReport"
]

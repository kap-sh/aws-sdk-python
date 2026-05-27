"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report_id

ImageUsageReportIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"
]

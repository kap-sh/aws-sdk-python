"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report_entry

ImageUsageReportEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_report_entry.ImageUsageReportEntry"
]

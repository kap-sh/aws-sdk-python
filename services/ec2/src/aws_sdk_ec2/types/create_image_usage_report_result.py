"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageUsageReportResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report_id


class CreateImageUsageReportResult(TypedDict):
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""

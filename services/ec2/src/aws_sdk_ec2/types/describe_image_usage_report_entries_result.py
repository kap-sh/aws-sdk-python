"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportEntriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report_entry_list
    import aws_sdk_ec2.types.string


class DescribeImageUsageReportEntriesResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    image_usage_report_entries: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_entry_list.ImageUsageReportEntryList"
    ]
    """<p>The content of the usage reports.</p>"""

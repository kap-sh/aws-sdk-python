"""Generated from Smithy shape ``com.amazonaws.ec2#DeclarativePoliciesReport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.report_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class DeclarativePoliciesReport(TypedDict):
    report_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the report.</p>"""
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the report is located.</p>"""
    s3_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for your S3 object.</p>"""
    target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The root ID, organizational unit ID, or account ID.</p> <p>Format:</p> <ul> <li> <p>For root: <code>r-ab12</code> </p> </li> <li> <p>For OU: <code>ou-ab12-cdef1234</code> </p> </li> <li> <p>For account: <code>123456789012</code> </p> </li> </ul>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the report generation started.</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time when the report generation ended.</p>"""
    status: NotRequired["aws_sdk_ec2.types.report_state.ReportState"]
    """<p>The current status of the report.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the report.</p>"""

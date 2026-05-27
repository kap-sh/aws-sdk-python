"""Generated from Smithy shape ``com.amazonaws.ec2#MetricPoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.float
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class MetricPoint(TypedDict):
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date for the metric point. The starting date for the metric point. The starting time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-10T12:00:00.000Z</code>.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date for the metric point. The ending time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-12T12:00:00.000Z</code>.</p>"""
    value: NotRequired["aws_sdk_ec2.types.float.Float"]
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the metric point.</p>"""

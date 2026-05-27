"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_event_window_cron_expression
    import aws_sdk_ec2.types.instance_event_window_time_range_request_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateInstanceEventWindowRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    time_ranges: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_time_range_request_set.InstanceEventWindowTimeRangeRequestSet"
    ]
    """<p>The time range for the event window. If you specify a time range, you can't specify a cron expression.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression for the event window, for example, <code>* 0-4,20-23 * * 1,5</code>. If you specify a cron expression, you can't specify a time range.</p> <p>Constraints:</p> <ul> <li> <p>Only hour and day of the week values are supported.</p> </li> <li> <p>For day of the week values, you can specify either integers <code>0</code> through <code>6</code>, or alternative single values <code>SUN</code> through <code>SAT</code>.</p> </li> <li> <p>The minute, month, and year must be specified by <code>*</code>.</p> </li> <li> <p>The hour value must be one or a multiple range, for example, <code>0-4</code> or <code>0-4,20-23</code>.</p> </li> <li> <p>Each hour range must be >= 2 hours, for example, <code>0-2</code> or <code>20-23</code>.</p> </li> <li> <p>The event window must be >= 4 hours. The combined total time ranges in the event window must be >= 4 hours.</p> </li> </ul> <p>For more information about cron expressions, see <a href=\"https://en.wikipedia.org/wiki/Cron\">cron</a> on the <i>Wikipedia website</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the event window.</p>"""

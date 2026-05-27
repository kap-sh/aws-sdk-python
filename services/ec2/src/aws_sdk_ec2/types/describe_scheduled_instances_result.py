"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance_set
    import aws_sdk_ec2.types.string


class DescribeScheduledInstancesResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token required to retrieve the next set of results. This value is <code>null</code> when there are no more results to return.</p>"""
    scheduled_instance_set: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_set.ScheduledInstanceSet"
    ]
    """<p>Information about the Scheduled Instances.</p>"""

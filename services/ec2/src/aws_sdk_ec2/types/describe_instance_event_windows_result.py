"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceEventWindowsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_set
    import aws_sdk_ec2.types.string


class DescribeInstanceEventWindowsResult(TypedDict):
    instance_event_windows: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_set.InstanceEventWindowSet"
    ]
    """<p>Information about the event windows.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""

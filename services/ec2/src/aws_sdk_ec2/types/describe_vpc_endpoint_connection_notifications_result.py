"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionNotificationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointConnectionNotificationsResult(TypedDict):
    connection_notification_set: NotRequired[
        "aws_sdk_ec2.types.connection_notification_set.ConnectionNotificationSet"
    ]
    """<p>The notifications.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

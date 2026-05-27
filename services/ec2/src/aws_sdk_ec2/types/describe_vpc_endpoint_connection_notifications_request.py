"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionNotificationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_id
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointConnectionNotificationsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_id: NotRequired[
        "aws_sdk_ec2.types.connection_notification_id.ConnectionNotificationId"
    ]
    """<p>The ID of the notification.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>connection-notification-arn</code> - The ARN of the SNS topic for the notification.</p> </li> <li> <p> <code>connection-notification-id</code> - The ID of the notification.</p> </li> <li> <p> <code>connection-notification-state</code> - The state of the notification (<code>Enabled</code> | <code>Disabled</code>).</p> </li> <li> <p> <code>connection-notification-type</code> - The type of notification (<code>Topic</code>).</p> </li> <li> <p> <code>service-id</code> - The ID of the endpoint service.</p> </li> <li> <p> <code>vpc-endpoint-id</code> - The ID of the VPC endpoint.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""

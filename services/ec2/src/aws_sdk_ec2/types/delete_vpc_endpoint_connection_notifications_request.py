"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointConnectionNotificationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_ids_list


class DeleteVpcEndpointConnectionNotificationsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_ids: NotRequired[
        "aws_sdk_ec2.types.connection_notification_ids_list.ConnectionNotificationIdsList"
    ]
    """<p>The IDs of the notifications.</p>"""

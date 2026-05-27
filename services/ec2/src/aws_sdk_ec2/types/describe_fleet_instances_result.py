"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.active_instance_set
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.string


class DescribeFleetInstancesResult(TypedDict):
    active_instances: NotRequired[
        "aws_sdk_ec2.types.active_instance_set.ActiveInstanceSet"
    ]
    """<p>The running instances. This list is refreshed periodically and might be out of date.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""

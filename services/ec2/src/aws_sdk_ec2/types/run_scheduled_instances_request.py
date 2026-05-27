"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_id
    import aws_sdk_ec2.types.scheduled_instances_launch_specification
    import aws_sdk_ec2.types.string


class RunScheduledInstancesRequest(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances.</p> <p>Default: 1</p>"""
    launch_specification: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_launch_specification.ScheduledInstancesLaunchSpecification"
    ]
    """<p>The launch specification. You must match the instance type, Availability Zone, network, and platform of the schedule that you purchased.</p>"""
    scheduled_instance_id: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_id.ScheduledInstanceId"
    ]
    """<p>The Scheduled Instance ID.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fleet_id_set


class DeleteFleetsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fleet_ids: NotRequired["aws_sdk_ec2.types.fleet_id_set.FleetIdSet"]
    """<p>The IDs of the EC2 Fleets.</p> <p>Constraints: In a single request, you can specify up to 25 <code>instant</code> fleet IDs and up to 100 <code>maintain</code> or <code>request</code> fleet IDs. </p>"""
    terminate_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to terminate the associated instances when the EC2 Fleet is deleted. The default is to terminate the instances.</p> <p>To let the instances continue to run after the EC2 Fleet is deleted, specify <code>no-terminate-instances</code>. Supported only for fleets of type <code>maintain</code> and <code>request</code>.</p> <p>For <code>instant</code> fleets, you cannot specify <code>NoTerminateInstances</code>. A deleted <code>instant</code> fleet with running instances is not supported.</p>"""

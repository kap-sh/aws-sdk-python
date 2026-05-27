"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.fleet_launch_template_config_list_request
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.target_capacity_specification_request


class ModifyFleetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    launch_template_configs: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_config_list_request.FleetLaunchTemplateConfigListRequest"
    ]
    """<p>The launch template and overrides.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
    target_capacity_specification: NotRequired[
        "aws_sdk_ec2.types.target_capacity_specification_request.TargetCapacitySpecificationRequest"
    ]
    """<p>The size of the EC2 Fleet.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""

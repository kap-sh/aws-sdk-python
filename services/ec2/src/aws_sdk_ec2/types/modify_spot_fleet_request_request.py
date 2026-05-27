"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySpotFleetRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.excess_capacity_termination_policy
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.launch_template_config_list
    import aws_sdk_ec2.types.spot_fleet_request_id
    import aws_sdk_ec2.types.string


class ModifySpotFleetRequestRequest(TypedDict):
    launch_template_configs: NotRequired[
        "aws_sdk_ec2.types.launch_template_config_list.LaunchTemplateConfigList"
    ]
    """<p>The launch template and overrides. You can only use this parameter if you specified a launch template (<code>LaunchTemplateConfigs</code>) in your Spot Fleet request. If you specified <code>LaunchSpecifications</code> in your Spot Fleet request, then omit this parameter.</p>"""
    on_demand_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of On-Demand Instances in the fleet.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    spot_fleet_request_id: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_id.SpotFleetRequestId"
    ]
    """<p>The ID of the Spot Fleet request.</p>"""
    target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the fleet.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "aws_sdk_ec2.types.excess_capacity_termination_policy.ExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#FleetData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.describe_fleets_error_set
    import aws_sdk_ec2.types.describe_fleets_instances_set
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.fleet_activity_status
    import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.fleet_launch_template_config_list
    import aws_sdk_ec2.types.fleet_state_code
    import aws_sdk_ec2.types.fleet_type
    import aws_sdk_ec2.types.on_demand_options
    import aws_sdk_ec2.types.reserved_capacity_options
    import aws_sdk_ec2.types.spot_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.target_capacity_specification


class FleetData(TypedDict):
    activity_status: NotRequired[
        "aws_sdk_ec2.types.fleet_activity_status.FleetActivityStatus"
    ]
    """<p>The progress of the EC2 Fleet.</p> <p>For fleets of type <code>instant</code>, the status is <code>fulfilled</code> after all requests are placed, regardless of whether target capacity is met (this is the only possible status for <code>instant</code> fleets).</p> <p>For fleets of type <code>request</code> or <code>maintain</code>, the status is <code>pending_fulfillment</code> after all requests are placed, <code>fulfilled</code> when the fleet size meets or exceeds target capacity, <code>pending_termination</code> while instances are terminating when fleet size is decreased, and <code>error</code> if there's an error.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation date and time of the EC2 Fleet.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
    fleet_state: NotRequired["aws_sdk_ec2.types.fleet_state_code.FleetStateCode"]
    """<p>The state of the EC2 Fleet.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p> <p>Constraints: Maximum 64 ASCII characters</p>"""
    excess_capacity_termination_policy: NotRequired[
        "aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units fulfilled by this request compared to the set target capacity.</p>"""
    fulfilled_on_demand_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units fulfilled by this request compared to the set target On-Demand capacity.</p>"""
    launch_template_configs: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_config_list.FleetLaunchTemplateConfigList"
    ]
    """<p>The launch template and overrides.</p>"""
    target_capacity_specification: NotRequired[
        "aws_sdk_ec2.types.target_capacity_specification.TargetCapacitySpecification"
    ]
    """<p>The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is <code>maintain</code>, you can specify a target capacity of 0 and add capacity later.</p>"""
    terminate_instances_with_expiration: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether running instances should be terminated when the EC2 Fleet expires. </p>"""
    type: NotRequired["aws_sdk_ec2.types.fleet_type.FleetType"]
    """<p>The type of request. Indicates whether the EC2 Fleet only <code>requests</code> the target capacity, or also attempts to <code>maintain</code> it. If you request a certain target capacity, EC2 Fleet only places the required requests; it does not attempt to replenish instances if capacity is diminished, and it does not submit requests in alternative capacity pools if capacity is unavailable. To maintain a certain target capacity, EC2 Fleet places the required requests to meet this target capacity. It also automatically replenishes any interrupted Spot Instances. Default: <code>maintain</code>.</p>"""
    valid_from: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The default is to start fulfilling the request immediately. </p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). At this point, no new instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date. </p>"""
    replace_unhealthy_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type <code>maintain</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks\">EC2 Fleet health checks</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    spot_options: NotRequired["aws_sdk_ec2.types.spot_options.SpotOptions"]
    """<p>The configuration of Spot Instances in an EC2 Fleet.</p>"""
    on_demand_options: NotRequired[
        "aws_sdk_ec2.types.on_demand_options.OnDemandOptions"
    ]
    """<p>The allocation strategy of On-Demand Instances in an EC2 Fleet.</p>"""
    reserved_capacity_options: NotRequired[
        "aws_sdk_ec2.types.reserved_capacity_options.ReservedCapacityOptions"
    ]
    """<p>Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to <code>reserved-capacity</code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for an EC2 Fleet resource.</p>"""
    errors: NotRequired[
        "aws_sdk_ec2.types.describe_fleets_error_set.DescribeFleetsErrorSet"
    ]
    """<p>Information about the instances that could not be launched by the fleet. Valid only when <b>Type</b> is set to <code>instant</code>.</p>"""
    instances: NotRequired[
        "aws_sdk_ec2.types.describe_fleets_instances_set.DescribeFleetsInstancesSet"
    ]
    """<p>Information about the instances that were launched by the fleet. Valid only when <b>Type</b> is set to <code>instant</code>.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy
    import aws_sdk_ec2.types.fleet_launch_template_config_list_request
    import aws_sdk_ec2.types.fleet_type
    import aws_sdk_ec2.types.on_demand_options_request
    import aws_sdk_ec2.types.reserved_capacity_options_request
    import aws_sdk_ec2.types.spot_options_request
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.target_capacity_specification_request


class CreateFleetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    spot_options: NotRequired[
        "aws_sdk_ec2.types.spot_options_request.SpotOptionsRequest"
    ]
    """<p>Describes the configuration of Spot Instances in an EC2 Fleet.</p>"""
    on_demand_options: NotRequired[
        "aws_sdk_ec2.types.on_demand_options_request.OnDemandOptionsRequest"
    ]
    """<p>Describes the configuration of On-Demand Instances in an EC2 Fleet.</p>"""
    reserved_capacity_options: NotRequired[
        "aws_sdk_ec2.types.reserved_capacity_options_request.ReservedCapacityOptionsRequest"
    ]
    """<p>Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to <code>reserved-capacity</code>.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    launch_template_configs: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_config_list_request.FleetLaunchTemplateConfigListRequest"
    ]
    """<p>The configuration for the EC2 Fleet.</p>"""
    target_capacity_specification: NotRequired[
        "aws_sdk_ec2.types.target_capacity_specification_request.TargetCapacitySpecificationRequest"
    ]
    """<p>The number of units to request.</p>"""
    terminate_instances_with_expiration: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether running instances should be terminated when the EC2 Fleet expires.</p>"""
    type: NotRequired["aws_sdk_ec2.types.fleet_type.FleetType"]
    """<p>The fleet type. The default value is <code>maintain</code>.</p> <ul> <li> <p> <code>maintain</code> - The EC2 Fleet places an asynchronous request for your desired capacity, and continues to maintain your desired Spot capacity by replenishing interrupted Spot Instances.</p> </li> <li> <p> <code>request</code> - The EC2 Fleet places an asynchronous one-time request for your desired capacity, but does submit Spot requests in alternative capacity pools if Spot capacity is unavailable, and does not maintain Spot capacity if Spot Instances are interrupted.</p> </li> <li> <p> <code>instant</code> - The EC2 Fleet places a synchronous one-time request for your desired capacity, and returns errors for any instances that could not be launched.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html\">EC2 Fleet request types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    valid_from: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The default is to start fulfilling the request immediately.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.</p>"""
    replace_unhealthy_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type <code>maintain</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks\">EC2 Fleet health checks</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the EC2 Fleet request on creation. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources\">Tag your resources</a>.</p> <p>If the fleet type is <code>instant</code>, specify a resource type of <code>fleet</code> to tag the fleet or <code>instance</code> to tag the instances at launch.</p> <p>If the fleet type is <code>maintain</code> or <code>request</code>, specify a resource type of <code>fleet</code> to tag the fleet. You cannot specify a resource type of <code>instance</code>. To tag instances at launch, specify the tags in a <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template\">launch template</a>.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""

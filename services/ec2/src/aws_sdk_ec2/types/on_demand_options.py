"""Generated from Smithy shape ``com.amazonaws.ec2#OnDemandOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_options
    import aws_sdk_ec2.types.fleet_on_demand_allocation_strategy
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class OnDemandOptions(TypedDict):
    allocation_strategy: NotRequired[
        "aws_sdk_ec2.types.fleet_on_demand_allocation_strategy.FleetOnDemandAllocationStrategy"
    ]
    """<p>The strategy that determines the order of the launch template overrides to use in fulfilling On-Demand capacity.</p> <p> <code>lowest-price</code> - EC2 Fleet uses price to determine the order, launching the lowest price first.</p> <p> <code>prioritized</code> - EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first.</p> <p>Default: <code>lowest-price</code> </p>"""
    capacity_reservation_options: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_options.CapacityReservationOptions"
    ]
    """<p>The strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    single_instance_type: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    single_availability_zone: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    min_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum target capacity for On-Demand Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.</p> <p>Constraints: Maximum value of <code>1000</code>. Supported only for fleets of type <code>instant</code>.</p> <p>At least one of the following must be specified: <code>SingleAvailabilityZone</code> | <code>SingleInstanceType</code> </p>"""
    max_total_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum amount per hour for On-Demand Instances that you're willing to pay.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>maxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>maxTotalPrice</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits\">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""

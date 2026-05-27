"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfigData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_strategy
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.excess_capacity_termination_policy
    import aws_sdk_ec2.types.fleet_type
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.launch_specs_list
    import aws_sdk_ec2.types.launch_template_config_list
    import aws_sdk_ec2.types.load_balancers_config
    import aws_sdk_ec2.types.on_demand_allocation_strategy
    import aws_sdk_ec2.types.spot_maintenance_strategies
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.target_capacity_unit_type


class SpotFleetRequestConfigData(TypedDict):
    allocation_strategy: NotRequired[
        "aws_sdk_ec2.types.allocation_strategy.AllocationStrategy"
    ]
    """<p>The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the Spot Fleet launch configuration. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html\">Allocation strategies for Spot Instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <dl> <dt>priceCapacityOptimized (recommended)</dt> <dd> <p>Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. Spot Fleet then requests Spot Instances from the lowest priced of these pools.</p> </dd> <dt>capacityOptimized</dt> <dd> <p>Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use <code>capacityOptimizedPrioritized</code>. Set a priority for each instance type by using the <code>Priority</code> parameter for <code>LaunchTemplateOverrides</code>. You can assign the same priority to different <code>LaunchTemplateOverrides</code>. EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. <code>capacityOptimizedPrioritized</code> is supported only if your Spot Fleet uses a launch template. Note that if the <code>OnDemandAllocationStrategy</code> is set to <code>prioritized</code>, the same priority is applied when fulfilling On-Demand capacity.</p> </dd> <dt>diversified</dt> <dd> <p>Spot Fleet requests instances from all of the Spot Instance pools that you specify.</p> </dd> <dt>lowestPrice (not recommended)</dt> <dd> <important> <p>We don't recommend the <code>lowestPrice</code> allocation strategy because it has the highest risk of interruption for your Spot Instances.</p> </important> <p>Spot Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, Spot Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.</p> </dd> </dl> <p>Default: <code>lowestPrice</code> </p>"""
    on_demand_allocation_strategy: NotRequired[
        "aws_sdk_ec2.types.on_demand_allocation_strategy.OnDemandAllocationStrategy"
    ]
    """<p>The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify <code>lowestPrice</code>, Spot Fleet uses price to determine the order, launching the lowest price first. If you specify <code>prioritized</code>, Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to <code>lowestPrice</code>.</p>"""
    spot_maintenance_strategies: NotRequired[
        "aws_sdk_ec2.types.spot_maintenance_strategies.SpotMaintenanceStrategies"
    ]
    """<p>The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "aws_sdk_ec2.types.excess_capacity_termination_policy.ExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if you decrease the target capacity of the Spot Fleet request below the current size of the Spot Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units fulfilled by this request compared to the set target capacity. You cannot set this value.</p>"""
    on_demand_fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.</p>"""
    iam_fleet_role: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that grants the Spot Fleet the permission to request, launch, terminate, and tag instances on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html#spot-fleet-prerequisites\">Spot Fleet prerequisites</a> in the <i>Amazon EC2 User Guide</i>. Spot Fleet can terminate Spot Instances on your behalf when you cancel its Spot Fleet request using <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests\">CancelSpotFleetRequests</a> or when the Spot Fleet request expires, if you set <code>TerminateInstancesWithExpiration</code>.</p>"""
    launch_specifications: NotRequired[
        "aws_sdk_ec2.types.launch_specs_list.LaunchSpecsList"
    ]
    """<p>The launch specifications for the Spot Fleet request. If you specify <code>LaunchSpecifications</code>, you can't specify <code>LaunchTemplateConfigs</code>. If you include On-Demand capacity in your request, you must use <code>LaunchTemplateConfigs</code>.</p> <note> <p>If an AMI specified in a launch specification is deregistered or disabled, no new instances can be launched from the AMI. For fleets of type <code>maintain</code>, the target capacity will not be maintained.</p> </note>"""
    launch_template_configs: NotRequired[
        "aws_sdk_ec2.types.launch_template_config_list.LaunchTemplateConfigList"
    ]
    """<p>The launch template and overrides. If you specify <code>LaunchTemplateConfigs</code>, you can't specify <code>LaunchSpecifications</code>. If you include On-Demand capacity in your request, you must use <code>LaunchTemplateConfigs</code>.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of units to request for the Spot Fleet. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is <code>maintain</code>, you can specify a target capacity of 0 and add capacity later.</p>"""
    on_demand_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is <code>maintain</code>, you can specify a target capacity of 0 and add capacity later.</p>"""
    on_demand_max_total_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum amount per hour for On-Demand Instances that you're willing to pay. You can use the <code>onDemandMaxTotalPrice</code> parameter, the <code>spotMaxTotalPrice</code> parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>onDemandMaxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>onDemandMaxTotalPrice</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits\">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""
    spot_max_total_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum amount per hour for Spot Instances that you're willing to pay. You can use the <code>spotMaxTotalPrice</code> parameter, the <code>onDemandMaxTotalPrice</code> parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.</p> <note> <p>If your fleet includes T instances that are configured as <code>unlimited</code>, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The <code>spotMaxTotalPrice</code> does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for <code>spotMaxTotalPrice</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits\">Surplus credits can incur charges</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>"""
    terminate_instances_with_expiration: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether running Spot Instances are terminated when the Spot Fleet request expires.</p>"""
    type: NotRequired["aws_sdk_ec2.types.fleet_type.FleetType"]
    """<p>The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is <code>request</code>, the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. When this value is <code>maintain</code>, the Spot Fleet maintains the target capacity. The Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: <code>maintain</code>. <code>instant</code> is listed but is not used by Spot Fleet.</p>"""
    valid_from: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date and time of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). By default, Amazon EC2 starts fulfilling the request immediately.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date and time of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). After the end date and time, no new Spot Instance requests are placed or able to fulfill the request. If no value is specified, the Spot Fleet request remains until you cancel it.</p>"""
    replace_unhealthy_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Spot Fleet should replace unhealthy instances.</p>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted. The default is <code>terminate</code>.</p>"""
    load_balancers_config: NotRequired[
        "aws_sdk_ec2.types.load_balancers_config.LoadBalancersConfig"
    ]
    """<p>One or more Classic Load Balancers and target groups to attach to the Spot Fleet request. Spot Fleet registers the running Spot Instances with the specified Classic Load Balancers and target groups.</p> <p>With Network Load Balancers, Spot Fleet cannot register instances that have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.</p>"""
    instance_pools_to_use_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot <b>AllocationStrategy</b> is set to <code>lowest-price</code>. Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.</p> <p>Note that Spot Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, Spot Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    target_capacity_unit_type: NotRequired[
        "aws_sdk_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity. You can specify this parameter only when using attribute-based instance type selection.</p> <p>Default: <code>units</code> (the number of instances)</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the Spot Fleet request on creation. The value for <code>ResourceType</code> must be <code>spot-fleet-request</code>, otherwise the Spot Fleet request fails. To tag instances at launch, specify the tags in the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template\">launch template</a> (valid only if you use <code>LaunchTemplateConfigs</code>) or in the <code> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetTagSpecification.html\">SpotFleetTagSpecification</a> </code> (valid only if you use <code>LaunchSpecifications</code>). For information about tagging after launch, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources\">Tag your resources</a>.</p>"""

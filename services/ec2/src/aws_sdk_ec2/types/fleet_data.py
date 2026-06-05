"""Generated from Smithy shape ``com.amazonaws.ec2#FleetData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "activity_status" in value:
        import aws_sdk_ec2.types.fleet_activity_status

        aws_sdk_ec2.types.fleet_activity_status.serialize_ec2_query(
            value["activity_status"], pairs, f"{prefix}.ActivityStatus"
        )
    if "create_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "fleet_id" in value:
        pairs.append((f"{prefix}.FleetId", str(value["fleet_id"])))
    if "fleet_state" in value:
        import aws_sdk_ec2.types.fleet_state_code

        aws_sdk_ec2.types.fleet_state_code.serialize_ec2_query(
            value["fleet_state"], pairs, f"{prefix}.FleetState"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "excess_capacity_termination_policy" in value:
        import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy

        aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.serialize_ec2_query(
            value["excess_capacity_termination_policy"],
            pairs,
            f"{prefix}.ExcessCapacityTerminationPolicy",
        )
    if "fulfilled_capacity" in value:
        pairs.append((f"{prefix}.FulfilledCapacity", str(value["fulfilled_capacity"])))
    if "fulfilled_on_demand_capacity" in value:
        pairs.append(
            (
                f"{prefix}.FulfilledOnDemandCapacity",
                str(value["fulfilled_on_demand_capacity"]),
            )
        )
    if "launch_template_configs" in value:
        import aws_sdk_ec2.types.fleet_launch_template_config_list

        aws_sdk_ec2.types.fleet_launch_template_config_list.serialize_ec2_query(
            value["launch_template_configs"], pairs, f"{prefix}.LaunchTemplateConfigs"
        )
    if "target_capacity_specification" in value:
        import aws_sdk_ec2.types.target_capacity_specification

        aws_sdk_ec2.types.target_capacity_specification.serialize_ec2_query(
            value["target_capacity_specification"],
            pairs,
            f"{prefix}.TargetCapacitySpecification",
        )
    if "terminate_instances_with_expiration" in value:
        pairs.append(
            (
                f"{prefix}.TerminateInstancesWithExpiration",
                "true" if value["terminate_instances_with_expiration"] else "false",
            )
        )
    if "type" in value:
        import aws_sdk_ec2.types.fleet_type

        aws_sdk_ec2.types.fleet_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "valid_from" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["valid_from"], pairs, f"{prefix}.ValidFrom"
        )
    if "valid_until" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{prefix}.ValidUntil"
        )
    if "replace_unhealthy_instances" in value:
        pairs.append(
            (
                f"{prefix}.ReplaceUnhealthyInstances",
                "true" if value["replace_unhealthy_instances"] else "false",
            )
        )
    if "spot_options" in value:
        import aws_sdk_ec2.types.spot_options

        aws_sdk_ec2.types.spot_options.serialize_ec2_query(
            value["spot_options"], pairs, f"{prefix}.SpotOptions"
        )
    if "on_demand_options" in value:
        import aws_sdk_ec2.types.on_demand_options

        aws_sdk_ec2.types.on_demand_options.serialize_ec2_query(
            value["on_demand_options"], pairs, f"{prefix}.OnDemandOptions"
        )
    if "reserved_capacity_options" in value:
        import aws_sdk_ec2.types.reserved_capacity_options

        aws_sdk_ec2.types.reserved_capacity_options.serialize_ec2_query(
            value["reserved_capacity_options"],
            pairs,
            f"{prefix}.ReservedCapacityOptions",
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "errors" in value:
        import aws_sdk_ec2.types.describe_fleets_error_set

        aws_sdk_ec2.types.describe_fleets_error_set.serialize_ec2_query(
            value["errors"], pairs, f"{prefix}.ErrorSet"
        )
    if "instances" in value:
        import aws_sdk_ec2.types.describe_fleets_instances_set

        aws_sdk_ec2.types.describe_fleets_instances_set.serialize_ec2_query(
            value["instances"], pairs, f"{prefix}.FleetInstanceSet"
        )
    if "context" in value:
        pairs.append((f"{prefix}.Context", str(value["context"])))


def deserialize_ec2_query(el: Element) -> FleetData:
    out: FleetData = {}  # type: ignore[typeddict-item]
    child_activity_status = el.find("ActivityStatus")
    if child_activity_status is not None:
        import aws_sdk_ec2.types.fleet_activity_status

        out["activity_status"] = (
            aws_sdk_ec2.types.fleet_activity_status.deserialize_ec2_query(
                child_activity_status
            )
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_ec2.types.date_time

        out["create_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_fleet_id = el.find("FleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    child_fleet_state = el.find("FleetState")
    if child_fleet_state is not None:
        import aws_sdk_ec2.types.fleet_state_code

        out["fleet_state"] = aws_sdk_ec2.types.fleet_state_code.deserialize_ec2_query(
            child_fleet_state
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_excess_capacity_termination_policy = el.find(
        "ExcessCapacityTerminationPolicy"
    )
    if child_excess_capacity_termination_policy is not None:
        import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy

        out["excess_capacity_termination_policy"] = (
            aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.deserialize_ec2_query(
                child_excess_capacity_termination_policy
            )
        )
    child_fulfilled_capacity = el.find("FulfilledCapacity")
    if child_fulfilled_capacity is not None:
        out["fulfilled_capacity"] = float(child_fulfilled_capacity.text or "")
    child_fulfilled_on_demand_capacity = el.find("FulfilledOnDemandCapacity")
    if child_fulfilled_on_demand_capacity is not None:
        out["fulfilled_on_demand_capacity"] = float(
            child_fulfilled_on_demand_capacity.text or ""
        )
    if el.find("LaunchTemplateConfigs") is not None:
        import aws_sdk_ec2.types.fleet_launch_template_config_list

        out["launch_template_configs"] = (
            aws_sdk_ec2.types.fleet_launch_template_config_list.deserialize_ec2_query(
                el, "LaunchTemplateConfigs"
            )
        )
    child_target_capacity_specification = el.find("TargetCapacitySpecification")
    if child_target_capacity_specification is not None:
        import aws_sdk_ec2.types.target_capacity_specification

        out["target_capacity_specification"] = (
            aws_sdk_ec2.types.target_capacity_specification.deserialize_ec2_query(
                child_target_capacity_specification
            )
        )
    child_terminate_instances_with_expiration = el.find(
        "TerminateInstancesWithExpiration"
    )
    if child_terminate_instances_with_expiration is not None:
        out["terminate_instances_with_expiration"] = (
            child_terminate_instances_with_expiration.text or ""
        ).lower() == "true"
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.fleet_type

        out["type"] = aws_sdk_ec2.types.fleet_type.deserialize_ec2_query(child_type)
    child_valid_from = el.find("ValidFrom")
    if child_valid_from is not None:
        import aws_sdk_ec2.types.date_time

        out["valid_from"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_valid_from
        )
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import aws_sdk_ec2.types.date_time

        out["valid_until"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_replace_unhealthy_instances = el.find("ReplaceUnhealthyInstances")
    if child_replace_unhealthy_instances is not None:
        out["replace_unhealthy_instances"] = (
            child_replace_unhealthy_instances.text or ""
        ).lower() == "true"
    child_spot_options = el.find("SpotOptions")
    if child_spot_options is not None:
        import aws_sdk_ec2.types.spot_options

        out["spot_options"] = aws_sdk_ec2.types.spot_options.deserialize_ec2_query(
            child_spot_options
        )
    child_on_demand_options = el.find("OnDemandOptions")
    if child_on_demand_options is not None:
        import aws_sdk_ec2.types.on_demand_options

        out["on_demand_options"] = (
            aws_sdk_ec2.types.on_demand_options.deserialize_ec2_query(
                child_on_demand_options
            )
        )
    child_reserved_capacity_options = el.find("ReservedCapacityOptions")
    if child_reserved_capacity_options is not None:
        import aws_sdk_ec2.types.reserved_capacity_options

        out["reserved_capacity_options"] = (
            aws_sdk_ec2.types.reserved_capacity_options.deserialize_ec2_query(
                child_reserved_capacity_options
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("ErrorSet") is not None:
        import aws_sdk_ec2.types.describe_fleets_error_set

        out["errors"] = (
            aws_sdk_ec2.types.describe_fleets_error_set.deserialize_ec2_query(
                el, "ErrorSet"
            )
        )
    if el.find("FleetInstanceSet") is not None:
        import aws_sdk_ec2.types.describe_fleets_instances_set

        out["instances"] = (
            aws_sdk_ec2.types.describe_fleets_instances_set.deserialize_ec2_query(
                el, "FleetInstanceSet"
            )
        )
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    return out

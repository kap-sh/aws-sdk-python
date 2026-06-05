"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySpotFleetRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySpotFleetRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_configs" in value:
        import aws_sdk_ec2.types.launch_template_config_list

        aws_sdk_ec2.types.launch_template_config_list.serialize_ec2_query(
            value["launch_template_configs"], pairs, f"{prefix}.LaunchTemplateConfigs"
        )
    if "on_demand_target_capacity" in value:
        pairs.append(
            (
                f"{prefix}.OnDemandTargetCapacity",
                str(value["on_demand_target_capacity"]),
            )
        )
    if "context" in value:
        pairs.append((f"{prefix}.Context", str(value["context"])))
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )
    if "target_capacity" in value:
        pairs.append((f"{prefix}.TargetCapacity", str(value["target_capacity"])))
    if "excess_capacity_termination_policy" in value:
        import aws_sdk_ec2.types.excess_capacity_termination_policy

        aws_sdk_ec2.types.excess_capacity_termination_policy.serialize_ec2_query(
            value["excess_capacity_termination_policy"],
            pairs,
            f"{prefix}.ExcessCapacityTerminationPolicy",
        )


def deserialize_ec2_query(el: Element) -> ModifySpotFleetRequestRequest:
    out: ModifySpotFleetRequestRequest = {}  # type: ignore[typeddict-item]
    if el.find("LaunchTemplateConfigs") is not None:
        import aws_sdk_ec2.types.launch_template_config_list

        out["launch_template_configs"] = (
            aws_sdk_ec2.types.launch_template_config_list.deserialize_ec2_query(
                el, "LaunchTemplateConfigs"
            )
        )
    child_on_demand_target_capacity = el.find("OnDemandTargetCapacity")
    if child_on_demand_target_capacity is not None:
        out["on_demand_target_capacity"] = int(
            child_on_demand_target_capacity.text or ""
        )
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    child_spot_fleet_request_id = el.find("SpotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    child_target_capacity = el.find("TargetCapacity")
    if child_target_capacity is not None:
        out["target_capacity"] = int(child_target_capacity.text or "")
    child_excess_capacity_termination_policy = el.find(
        "ExcessCapacityTerminationPolicy"
    )
    if child_excess_capacity_termination_policy is not None:
        import aws_sdk_ec2.types.excess_capacity_termination_policy

        out["excess_capacity_termination_policy"] = (
            aws_sdk_ec2.types.excess_capacity_termination_policy.deserialize_ec2_query(
                child_excess_capacity_termination_policy
            )
        )
    return out

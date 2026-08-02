"""Generated from Smithy shape ``com.amazonaws.ec2#TargetCapacitySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.default_target_capacity_type
    import capo_ec2.types.integer
    import capo_ec2.types.target_capacity_unit_type


class TargetCapacitySpecification(TypedDict, closed=True):
    total_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of units to request, filled the default target capacity type.</p>"""
    on_demand_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of On-Demand units to request. If you specify a target capacity for Spot units, you cannot specify a target capacity for On-Demand units.</p>"""
    spot_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of Spot units to launch. If you specify a target capacity for On-Demand units, you cannot specify a target capacity for Spot units.</p>"""
    default_target_capacity_type: NotRequired[
        "capo_ec2.types.default_target_capacity_type.DefaultTargetCapacityType"
    ]
    """<p>The default target capacity type.</p>"""
    target_capacity_unit_type: NotRequired[
        "capo_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetCapacitySpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "total_target_capacity" in value:
        pairs.append(
            (f"{key_prefix}TotalTargetCapacity", str(value["total_target_capacity"]))
        )
    if "on_demand_target_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandTargetCapacity",
                str(value["on_demand_target_capacity"]),
            )
        )
    if "spot_target_capacity" in value:
        pairs.append(
            (f"{key_prefix}SpotTargetCapacity", str(value["spot_target_capacity"]))
        )
    if "default_target_capacity_type" in value:
        import capo_ec2.types.default_target_capacity_type

        capo_ec2.types.default_target_capacity_type.serialize_ec2_query(
            value["default_target_capacity_type"],
            pairs,
            f"{key_prefix}DefaultTargetCapacityType",
        )
    if "target_capacity_unit_type" in value:
        import capo_ec2.types.target_capacity_unit_type

        capo_ec2.types.target_capacity_unit_type.serialize_ec2_query(
            value["target_capacity_unit_type"],
            pairs,
            f"{key_prefix}TargetCapacityUnitType",
        )


def deserialize_ec2_query(el: Element) -> TargetCapacitySpecification:
    out: TargetCapacitySpecification = {}  # type: ignore[typeddict-item]
    child_total_target_capacity = el.find("TotalTargetCapacity")
    if child_total_target_capacity is not None:
        out["total_target_capacity"] = int(child_total_target_capacity.text or "")
    child_on_demand_target_capacity = el.find("OnDemandTargetCapacity")
    if child_on_demand_target_capacity is not None:
        out["on_demand_target_capacity"] = int(
            child_on_demand_target_capacity.text or ""
        )
    child_spot_target_capacity = el.find("SpotTargetCapacity")
    if child_spot_target_capacity is not None:
        out["spot_target_capacity"] = int(child_spot_target_capacity.text or "")
    child_default_target_capacity_type = el.find("DefaultTargetCapacityType")
    if child_default_target_capacity_type is not None:
        import capo_ec2.types.default_target_capacity_type

        out["default_target_capacity_type"] = (
            capo_ec2.types.default_target_capacity_type.deserialize_ec2_query(
                child_default_target_capacity_type
            )
        )
    child_target_capacity_unit_type = el.find("TargetCapacityUnitType")
    if child_target_capacity_unit_type is not None:
        import capo_ec2.types.target_capacity_unit_type

        out["target_capacity_unit_type"] = (
            capo_ec2.types.target_capacity_unit_type.deserialize_ec2_query(
                child_target_capacity_unit_type
            )
        )
    return out

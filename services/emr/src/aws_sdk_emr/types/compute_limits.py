"""Generated from Smithy shape ``com.amazonaws.emr#ComputeLimits``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.compute_limits_unit_type
    import aws_sdk_emr.types.integer


class ComputeLimits(TypedDict):
    unit_type: NotRequired[
        "aws_sdk_emr.types.compute_limits_unit_type.ComputeLimitsUnitType"
    ]
    """<p> The unit type used for specifying a managed scaling policy. </p>"""
    minimum_capacity_units: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p> The lower boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration. </p>"""
    maximum_capacity_units: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p> The upper boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration. </p>"""
    maximum_on_demand_capacity_units: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p> The upper boundary of On-Demand Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot Instances. </p>"""
    maximum_core_capacity_units: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p> The upper boundary of Amazon EC2 units for core node type in a cluster. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeLimits) -> dict:
    out: dict = {}
    if "unit_type" in value:
        import aws_sdk_emr.types.compute_limits_unit_type

        out["UnitType"] = (
            aws_sdk_emr.types.compute_limits_unit_type.serialize_aws_json_1_1(
                value["unit_type"]
            )
        )
    if "minimum_capacity_units" in value:
        out["MinimumCapacityUnits"] = value["minimum_capacity_units"]
    if "maximum_capacity_units" in value:
        out["MaximumCapacityUnits"] = value["maximum_capacity_units"]
    if "maximum_on_demand_capacity_units" in value:
        out["MaximumOnDemandCapacityUnits"] = value["maximum_on_demand_capacity_units"]
    if "maximum_core_capacity_units" in value:
        out["MaximumCoreCapacityUnits"] = value["maximum_core_capacity_units"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeLimits:
    out: ComputeLimits = {}  # type: ignore[typeddict-item]
    if "UnitType" in data:
        import aws_sdk_emr.types.compute_limits_unit_type

        out["unit_type"] = (
            aws_sdk_emr.types.compute_limits_unit_type.deserialize_aws_json_1_1(
                data["UnitType"]
            )
        )
    if "MinimumCapacityUnits" in data:
        out["minimum_capacity_units"] = data["MinimumCapacityUnits"]
    if "MaximumCapacityUnits" in data:
        out["maximum_capacity_units"] = data["MaximumCapacityUnits"]
    if "MaximumOnDemandCapacityUnits" in data:
        out["maximum_on_demand_capacity_units"] = data["MaximumOnDemandCapacityUnits"]
    if "MaximumCoreCapacityUnits" in data:
        out["maximum_core_capacity_units"] = data["MaximumCoreCapacityUnits"]
    return out

"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandProvisioningSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.on_demand_capacity_reservation_options
    import aws_sdk_emr.types.on_demand_provisioning_allocation_strategy


class OnDemandProvisioningSpecification(TypedDict):
    allocation_strategy: NotRequired[
        "aws_sdk_emr.types.on_demand_provisioning_allocation_strategy.OnDemandProvisioningAllocationStrategy"
    ]
    """<p>Specifies the strategy to use in launching On-Demand instance fleets. Available options are <code>lowest-price</code> and <code>prioritized</code>. <code>lowest-price</code> specifies to launch the instances with the lowest price first, and <code>prioritized</code> specifies that Amazon EMR should launch the instances with the highest priority first. The default is <code>lowest-price</code>.</p>"""
    capacity_reservation_options: NotRequired[
        "aws_sdk_emr.types.on_demand_capacity_reservation_options.OnDemandCapacityReservationOptions"
    ]
    """<p>The launch specification for On-Demand instances in the instance fleet, which determines the allocation strategy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandProvisioningSpecification) -> dict:
    out: dict = {}
    if "allocation_strategy" in value:
        import aws_sdk_emr.types.on_demand_provisioning_allocation_strategy

        out["AllocationStrategy"] = (
            aws_sdk_emr.types.on_demand_provisioning_allocation_strategy.serialize_aws_json_1_1(
                value["allocation_strategy"]
            )
        )
    if "capacity_reservation_options" in value:
        import aws_sdk_emr.types.on_demand_capacity_reservation_options

        out["CapacityReservationOptions"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_options.serialize_aws_json_1_1(
                value["capacity_reservation_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnDemandProvisioningSpecification:
    out: OnDemandProvisioningSpecification = {}  # type: ignore[typeddict-item]
    if "AllocationStrategy" in data:
        import aws_sdk_emr.types.on_demand_provisioning_allocation_strategy

        out["allocation_strategy"] = (
            aws_sdk_emr.types.on_demand_provisioning_allocation_strategy.deserialize_aws_json_1_1(
                data["AllocationStrategy"]
            )
        )
    if "CapacityReservationOptions" in data:
        import aws_sdk_emr.types.on_demand_capacity_reservation_options

        out["capacity_reservation_options"] = (
            aws_sdk_emr.types.on_demand_capacity_reservation_options.deserialize_aws_json_1_1(
                data["CapacityReservationOptions"]
            )
        )
    return out

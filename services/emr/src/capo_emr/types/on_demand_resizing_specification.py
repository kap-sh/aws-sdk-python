"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandResizingSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.on_demand_capacity_reservation_options
    import capo_emr.types.on_demand_provisioning_allocation_strategy
    import capo_emr.types.whole_number


class OnDemandResizingSpecification(TypedDict, closed=True):
    timeout_duration_minutes: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>On-Demand resize timeout in minutes. If On-Demand Instances are not provisioned within this time, the resize workflow stops. The minimum value is 5 minutes, and the maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.</p>"""
    allocation_strategy: NotRequired[
        "capo_emr.types.on_demand_provisioning_allocation_strategy.OnDemandProvisioningAllocationStrategy"
    ]
    """<p>Specifies the allocation strategy to use to launch On-Demand instances during a resize. The default is <code>lowest-price</code>.</p>"""
    capacity_reservation_options: NotRequired[
        "capo_emr.types.on_demand_capacity_reservation_options.OnDemandCapacityReservationOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandResizingSpecification) -> dict:
    out: dict = {}
    if "timeout_duration_minutes" in value:
        out["TimeoutDurationMinutes"] = value["timeout_duration_minutes"]
    if "allocation_strategy" in value:
        import capo_emr.types.on_demand_provisioning_allocation_strategy

        out["AllocationStrategy"] = (
            capo_emr.types.on_demand_provisioning_allocation_strategy.serialize_aws_json_1_1(
                value["allocation_strategy"]
            )
        )
    if "capacity_reservation_options" in value:
        import capo_emr.types.on_demand_capacity_reservation_options

        out["CapacityReservationOptions"] = (
            capo_emr.types.on_demand_capacity_reservation_options.serialize_aws_json_1_1(
                value["capacity_reservation_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnDemandResizingSpecification:
    out: OnDemandResizingSpecification = {}  # type: ignore[typeddict-item]
    if "TimeoutDurationMinutes" in data:
        out["timeout_duration_minutes"] = data["TimeoutDurationMinutes"]
    if "AllocationStrategy" in data:
        import capo_emr.types.on_demand_provisioning_allocation_strategy

        out["allocation_strategy"] = (
            capo_emr.types.on_demand_provisioning_allocation_strategy.deserialize_aws_json_1_1(
                data["AllocationStrategy"]
            )
        )
    if "CapacityReservationOptions" in data:
        import capo_emr.types.on_demand_capacity_reservation_options

        out["capacity_reservation_options"] = (
            capo_emr.types.on_demand_capacity_reservation_options.deserialize_aws_json_1_1(
                data["CapacityReservationOptions"]
            )
        )
    return out

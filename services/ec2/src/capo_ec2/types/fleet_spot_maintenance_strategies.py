"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSpotMaintenanceStrategies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_spot_capacity_rebalance


class FleetSpotMaintenanceStrategies(TypedDict, closed=True):
    capacity_rebalance: NotRequired[
        "capo_ec2.types.fleet_spot_capacity_rebalance.FleetSpotCapacityRebalance"
    ]
    """<p>The strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetSpotMaintenanceStrategies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_rebalance" in value:
        import capo_ec2.types.fleet_spot_capacity_rebalance

        capo_ec2.types.fleet_spot_capacity_rebalance.serialize_ec2_query(
            value["capacity_rebalance"], pairs, f"{prefix}.CapacityRebalance"
        )


def deserialize_ec2_query(el: Element) -> FleetSpotMaintenanceStrategies:
    out: FleetSpotMaintenanceStrategies = {}  # type: ignore[typeddict-item]
    child_capacity_rebalance = el.find("CapacityRebalance")
    if child_capacity_rebalance is not None:
        import capo_ec2.types.fleet_spot_capacity_rebalance

        out["capacity_rebalance"] = (
            capo_ec2.types.fleet_spot_capacity_rebalance.deserialize_ec2_query(
                child_capacity_rebalance
            )
        )
    return out

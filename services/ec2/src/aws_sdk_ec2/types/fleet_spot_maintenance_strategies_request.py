"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSpotMaintenanceStrategiesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request


class FleetSpotMaintenanceStrategiesRequest(TypedDict):
    capacity_rebalance: NotRequired[
        "aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request.FleetSpotCapacityRebalanceRequest"
    ]
    """<p>The strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetSpotMaintenanceStrategiesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_rebalance" in value:
        import aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request

        aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request.serialize_ec2_query(
            value["capacity_rebalance"], pairs, f"{prefix}.CapacityRebalance"
        )


def deserialize_ec2_query(el: Element) -> FleetSpotMaintenanceStrategiesRequest:
    out: FleetSpotMaintenanceStrategiesRequest = {}  # type: ignore[typeddict-item]
    child_capacity_rebalance = el.find("CapacityRebalance")
    if child_capacity_rebalance is not None:
        import aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request

        out["capacity_rebalance"] = (
            aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request.deserialize_ec2_query(
                child_capacity_rebalance
            )
        )
    return out

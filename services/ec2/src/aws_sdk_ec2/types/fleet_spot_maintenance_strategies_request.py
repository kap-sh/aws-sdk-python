"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSpotMaintenanceStrategiesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request


class FleetSpotMaintenanceStrategiesRequest(TypedDict):
    capacity_rebalance: NotRequired[
        "aws_sdk_ec2.types.fleet_spot_capacity_rebalance_request.FleetSpotCapacityRebalanceRequest"
    ]
    """<p>The strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted.</p>"""

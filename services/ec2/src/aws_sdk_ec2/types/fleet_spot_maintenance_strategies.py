"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSpotMaintenanceStrategies``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_spot_capacity_rebalance


class FleetSpotMaintenanceStrategies(TypedDict):
    capacity_rebalance: NotRequired[
        "aws_sdk_ec2.types.fleet_spot_capacity_rebalance.FleetSpotCapacityRebalance"
    ]
    """<p>The strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#SpotMaintenanceStrategies``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_capacity_rebalance


class SpotMaintenanceStrategies(TypedDict):
    capacity_rebalance: NotRequired[
        "aws_sdk_ec2.types.spot_capacity_rebalance.SpotCapacityRebalance"
    ]
    """<p>The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html\">Capacity rebalancing</a> in the <i>Amazon EC2 User Guide</i>.</p>"""

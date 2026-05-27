"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item

CancelSpotFleetRequestsErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item.CancelSpotFleetRequestsErrorItem"
]

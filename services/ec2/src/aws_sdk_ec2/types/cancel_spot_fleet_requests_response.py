"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set


class CancelSpotFleetRequestsResponse(TypedDict):
    successful_fleet_requests: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_fleet_requests_success_set.CancelSpotFleetRequestsSuccessSet"
    ]
    """<p>Information about the Spot Fleet requests that are successfully canceled.</p>"""
    unsuccessful_fleet_requests: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_fleet_requests_error_set.CancelSpotFleetRequestsErrorSet"
    ]
    """<p>Information about the Spot Fleet requests that are not successfully canceled.</p>"""

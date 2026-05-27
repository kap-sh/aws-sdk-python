"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error
    import aws_sdk_ec2.types.string


class CancelSpotFleetRequestsErrorItem(TypedDict):
    error: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_fleet_requests_error.CancelSpotFleetRequestsError"
    ]
    """<p>The error.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""

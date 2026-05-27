"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsSuccessItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.batch_state
    import aws_sdk_ec2.types.string


class CancelSpotFleetRequestsSuccessItem(TypedDict):
    current_spot_fleet_request_state: NotRequired[
        "aws_sdk_ec2.types.batch_state.BatchState"
    ]
    """<p>The current state of the Spot Fleet request.</p>"""
    previous_spot_fleet_request_state: NotRequired[
        "aws_sdk_ec2.types.batch_state.BatchState"
    ]
    """<p>The previous state of the Spot Fleet request.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""

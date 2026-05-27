"""Generated from Smithy shape ``com.amazonaws.ec2#CancelledSpotInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_instance_request_state
    import aws_sdk_ec2.types.string


class CancelledSpotInstanceRequest(TypedDict):
    spot_instance_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_instance_request_state.CancelSpotInstanceRequestState"
    ]
    """<p>The state of the Spot Instance request.</p>"""

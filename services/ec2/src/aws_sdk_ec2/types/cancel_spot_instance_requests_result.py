"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequestsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancelled_spot_instance_request_list


class CancelSpotInstanceRequestsResult(TypedDict):
    cancelled_spot_instance_requests: NotRequired[
        "aws_sdk_ec2.types.cancelled_spot_instance_request_list.CancelledSpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""

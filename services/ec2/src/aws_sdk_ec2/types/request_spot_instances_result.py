"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_list


class RequestSpotInstancesResult(TypedDict):
    spot_instance_requests: NotRequired[
        "aws_sdk_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""

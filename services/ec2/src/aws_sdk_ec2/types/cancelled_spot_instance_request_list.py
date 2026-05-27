"""Generated from Smithy shape ``com.amazonaws.ec2#CancelledSpotInstanceRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancelled_spot_instance_request

CancelledSpotInstanceRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.cancelled_spot_instance_request.CancelledSpotInstanceRequest"
]

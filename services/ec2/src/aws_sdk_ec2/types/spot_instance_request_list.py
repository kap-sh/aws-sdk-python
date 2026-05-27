"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request

SpotInstanceRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_instance_request.SpotInstanceRequest"
]

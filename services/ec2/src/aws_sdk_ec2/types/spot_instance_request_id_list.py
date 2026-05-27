"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequestIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_id

SpotInstanceRequestIdList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_instance_request_id.SpotInstanceRequestId"
]

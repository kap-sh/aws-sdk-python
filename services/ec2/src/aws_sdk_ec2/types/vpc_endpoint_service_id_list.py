"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointServiceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_endpoint_service_id

VpcEndpointServiceIdList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
]

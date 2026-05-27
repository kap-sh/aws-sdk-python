"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_endpoint_id

VpcEndpointIdList: TypeAlias = list["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]

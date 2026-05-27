"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_endpoint

VpcEndpointSet: TypeAlias = list["aws_sdk_ec2.types.vpc_endpoint.VpcEndpoint"]

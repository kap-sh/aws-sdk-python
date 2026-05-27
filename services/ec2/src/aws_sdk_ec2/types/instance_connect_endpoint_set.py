"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint

InstanceConnectEndpointSet: TypeAlias = list[
    "aws_sdk_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
]

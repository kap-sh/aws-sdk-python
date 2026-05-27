"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointPortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range

CreateVerifiedAccessEndpointPortRangeList: TypeAlias = list[
    "aws_sdk_ec2.types.create_verified_access_endpoint_port_range.CreateVerifiedAccessEndpointPortRange"
]

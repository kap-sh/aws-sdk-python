"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointPortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range

ModifyVerifiedAccessEndpointPortRangeList: TypeAlias = list[
    "aws_sdk_ec2.types.modify_verified_access_endpoint_port_range.ModifyVerifiedAccessEndpointPortRange"
]

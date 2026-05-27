"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway

EgressOnlyInternetGatewayList: TypeAlias = list[
    "aws_sdk_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
]

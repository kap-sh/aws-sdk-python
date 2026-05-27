"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGatewayIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway_id

EgressOnlyInternetGatewayIdList: TypeAlias = list[
    "aws_sdk_ec2.types.egress_only_internet_gateway_id.EgressOnlyInternetGatewayId"
]

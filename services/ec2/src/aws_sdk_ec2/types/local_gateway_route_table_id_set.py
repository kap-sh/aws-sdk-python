"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_routetable_id

LocalGatewayRouteTableIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
]

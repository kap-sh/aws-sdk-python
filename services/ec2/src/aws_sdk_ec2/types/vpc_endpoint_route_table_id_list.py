"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointRouteTableIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_id

VpcEndpointRouteTableIdList: TypeAlias = list[
    "aws_sdk_ec2.types.route_table_id.RouteTableId"
]

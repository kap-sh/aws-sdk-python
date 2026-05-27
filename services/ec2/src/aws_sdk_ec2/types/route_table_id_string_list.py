"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_id

RouteTableIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.route_table_id.RouteTableId"
]

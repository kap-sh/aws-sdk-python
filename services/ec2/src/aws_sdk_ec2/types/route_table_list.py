"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table

RouteTableList: TypeAlias = list["aws_sdk_ec2.types.route_table.RouteTable"]

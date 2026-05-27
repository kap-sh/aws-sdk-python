"""Generated from Smithy shape ``com.amazonaws.ec2#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route

RouteList: TypeAlias = list["aws_sdk_ec2.types.route.Route"]

"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_association

RouteServerAssociationsList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_association.RouteServerAssociation"
]

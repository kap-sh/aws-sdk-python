"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association

RouteTableAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.route_table_association.RouteTableAssociation"
]

"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVpcAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayRouteTableVpcAssociation(TypedDict):
    local_gateway_route_table_vpc_association_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id.LocalGatewayRouteTableVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    local_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table for the association.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route table for the association.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the association.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the association.</p>"""

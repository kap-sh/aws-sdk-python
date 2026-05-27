"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTable``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.propagating_vgw_list
    import aws_sdk_ec2.types.route_list
    import aws_sdk_ec2.types.route_table_association_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class RouteTable(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.route_table_association_list.RouteTableAssociationList"
    ]
    """<p>The associations between the route table and your subnets or gateways.</p>"""
    propagating_vgws: NotRequired[
        "aws_sdk_ec2.types.propagating_vgw_list.PropagatingVgwList"
    ]
    """<p>Any virtual private gateway (VGW) propagating routes.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the route table.</p>"""
    routes: NotRequired["aws_sdk_ec2.types.route_list.RouteList"]
    """<p>The routes in the route table.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route table.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the route table.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_table_association_state
    import aws_sdk_ec2.types.string


class RouteTableAssociation(TypedDict):
    main: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the main route table.</p>"""
    route_table_association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the route table.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet. A subnet ID is not returned for an implicit association.</p>"""
    gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the internet gateway or virtual private gateway.</p>"""
    public_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to Amazon Web Services with BYOIP.</p>"""
    association_state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""

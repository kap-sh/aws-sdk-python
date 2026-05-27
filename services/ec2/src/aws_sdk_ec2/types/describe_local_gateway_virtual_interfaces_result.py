"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayVirtualInterfacesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayVirtualInterfacesResult(TypedDict):
    local_gateway_virtual_interfaces: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_set.LocalGatewayVirtualInterfaceSet"
    ]
    """<p>Information about the virtual interfaces.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

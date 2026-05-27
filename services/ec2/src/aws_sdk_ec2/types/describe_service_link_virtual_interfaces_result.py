"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeServiceLinkVirtualInterfacesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_link_virtual_interface_set
    import aws_sdk_ec2.types.string


class DescribeServiceLinkVirtualInterfacesResult(TypedDict):
    service_link_virtual_interfaces: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_set.ServiceLinkVirtualInterfaceSet"
    ]
    """<p>Describes the service link virtual interfaces.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

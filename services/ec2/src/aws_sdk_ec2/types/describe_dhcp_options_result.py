"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeDhcpOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_options_list
    import aws_sdk_ec2.types.string


class DescribeDhcpOptionsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    dhcp_options: NotRequired["aws_sdk_ec2.types.dhcp_options_list.DhcpOptionsList"]
    """<p>Information about the DHCP options sets.</p>"""

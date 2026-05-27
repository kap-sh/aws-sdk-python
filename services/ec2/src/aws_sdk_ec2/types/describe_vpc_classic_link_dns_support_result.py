"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkDnsSupportResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_link_dns_support_list
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token


class DescribeVpcClassicLinkDnsSupportResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token.DescribeVpcClassicLinkDnsSupportNextToken"
    ]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    vpcs: NotRequired[
        "aws_sdk_ec2.types.classic_link_dns_support_list.ClassicLinkDnsSupportList"
    ]
    """<p>Information about the ClassicLink DNS support status of the VPCs.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_classic_link_list


class DescribeVpcClassicLinkResult(TypedDict):
    vpcs: NotRequired["aws_sdk_ec2.types.vpc_classic_link_list.VpcClassicLinkList"]
    """<p>The ClassicLink status of the VPCs.</p>"""

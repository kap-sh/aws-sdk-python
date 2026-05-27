"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamResourceDiscoveriesResult(TypedDict):
    ipam_resource_discoveries: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_set.IpamResourceDiscoverySet"
    ]
    """<p>The resource discoveries.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

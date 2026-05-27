"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredResourceCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_resource_cidr_set
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredResourceCidrsResult(TypedDict):
    ipam_discovered_resource_cidrs: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_resource_cidr_set.IpamDiscoveredResourceCidrSet"
    ]
    """<p>Discovered resource CIDRs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""

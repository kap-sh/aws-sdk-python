"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveryAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_association_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamResourceDiscoveryAssociationsResult(TypedDict):
    ipam_resource_discovery_associations: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_set.IpamResourceDiscoveryAssociationSet"
    ]
    """<p>The resource discovery associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

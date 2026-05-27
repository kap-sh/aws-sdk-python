"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedIpv6PoolCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_cidr_association_set
    import aws_sdk_ec2.types.string


class GetAssociatedIpv6PoolCidrsResult(TypedDict):
    ipv6_cidr_associations: NotRequired[
        "aws_sdk_ec2.types.ipv6_cidr_association_set.Ipv6CidrAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR block associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

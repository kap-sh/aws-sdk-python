"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredPublicAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_public_address_set
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredPublicAddressesResult(TypedDict):
    ipam_discovered_public_addresses: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_public_address_set.IpamDiscoveredPublicAddressSet"
    ]
    """<p>IPAM discovered public addresses.</p>"""
    oldest_sample_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The oldest successful resource discovery time.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4Pool``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.public_ipv4_pool_range_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class PublicIpv4Pool(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the address pool.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the address pool.</p>"""
    pool_address_ranges: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_range_set.PublicIpv4PoolRangeSet"
    ]
    """<p>The address ranges.</p>"""
    total_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of addresses.</p>"""
    total_available_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of available addresses.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the location from which the address pool is advertised. A network border group is a unique set of Availability Zones or Local Zones from where Amazon Web Services advertises public IP addresses.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags for the address pool.</p>"""

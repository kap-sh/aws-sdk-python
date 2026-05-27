"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePublicIpv4PoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_ec2_id


class CreatePublicIpv4PoolResult(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the public IPv4 pool.</p>"""

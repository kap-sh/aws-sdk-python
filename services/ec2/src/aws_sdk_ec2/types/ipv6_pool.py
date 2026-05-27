"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6Pool``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.pool_cidr_blocks_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class Ipv6Pool(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the address pool.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the address pool.</p>"""
    pool_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.pool_cidr_blocks_set.PoolCidrBlocksSet"
    ]
    """<p>The CIDR blocks for the address pool.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags for the address pool.</p>"""

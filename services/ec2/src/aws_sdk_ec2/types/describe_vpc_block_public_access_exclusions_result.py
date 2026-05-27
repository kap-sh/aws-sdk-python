"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessExclusionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_list


class DescribeVpcBlockPublicAccessExclusionsResult(TypedDict):
    vpc_block_public_access_exclusions: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_list.VpcBlockPublicAccessExclusionList"
    ]
    """<p>Details related to the exclusions.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""

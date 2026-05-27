"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondarySubnetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet_list
    import aws_sdk_ec2.types.string


class DescribeSecondarySubnetsResult(TypedDict):
    secondary_subnets: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_list.SecondarySubnetList"
    ]
    """<p>Information about the secondary subnets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

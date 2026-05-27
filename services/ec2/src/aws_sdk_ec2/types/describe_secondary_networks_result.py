"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryNetworksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_list
    import aws_sdk_ec2.types.string


class DescribeSecondaryNetworksResult(TypedDict):
    secondary_networks: NotRequired[
        "aws_sdk_ec2.types.secondary_network_list.SecondaryNetworkList"
    ]
    """<p>Information about the secondary networks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

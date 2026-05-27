"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredAccountsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_account_set
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredAccountsResult(TypedDict):
    ipam_discovered_accounts: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_account_set.IpamDiscoveredAccountSet"
    ]
    """<p>Discovered accounts.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""

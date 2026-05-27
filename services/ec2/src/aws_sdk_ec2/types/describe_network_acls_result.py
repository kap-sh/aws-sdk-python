"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkAclsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl_list
    import aws_sdk_ec2.types.string


class DescribeNetworkAclsResult(TypedDict):
    network_acls: NotRequired["aws_sdk_ec2.types.network_acl_list.NetworkAclList"]
    """<p>Information about the network ACLs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""

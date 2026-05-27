"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_list
    import aws_sdk_ec2.types.string


class DescribeHostsResult(TypedDict):
    hosts: NotRequired["aws_sdk_ec2.types.host_list.HostList"]
    """<p>Information about the Dedicated Hosts.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

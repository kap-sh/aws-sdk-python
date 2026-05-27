"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacHostsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_host_list
    import aws_sdk_ec2.types.string


class DescribeMacHostsResult(TypedDict):
    mac_hosts: NotRequired["aws_sdk_ec2.types.mac_host_list.MacHostList"]
    """<p> Information about the EC2 Mac Dedicated Hosts. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""

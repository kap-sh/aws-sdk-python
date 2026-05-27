"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface
    import aws_sdk_ec2.types.string


class CreateNetworkInterfaceResult(TypedDict):
    network_interface: NotRequired[
        "aws_sdk_ec2.types.network_interface.NetworkInterface"
    ]
    """<p>Information about the network interface.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfaceAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_attribute
    import aws_sdk_ec2.types.network_interface_id


class DescribeNetworkInterfaceAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.network_interface_attribute.NetworkInterfaceAttribute"
    ]
    """<p>The attribute of the network interface. This parameter is required.</p>"""

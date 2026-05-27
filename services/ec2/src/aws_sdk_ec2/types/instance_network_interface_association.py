"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceNetworkInterfaceAssociation(TypedDict):
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address associated with the network interface.</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address associated with the network interface.</p>"""
    ip_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner of the Elastic IP address.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public DNS name.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public IP address or Elastic IP address bound to the network interface.</p>"""

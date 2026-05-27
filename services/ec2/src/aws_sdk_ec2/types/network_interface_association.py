"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class NetworkInterfaceAssociation(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID.</p>"""
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association ID.</p>"""
    ip_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Elastic IP address owner.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public DNS name.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address of the Elastic IP address bound to the network interface.</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address associated with the network interface.</p>"""
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address associated with the network interface.</p> <p>This option is only available when the network interface is in a subnet which is associated with a Wavelength Zone.</p>"""

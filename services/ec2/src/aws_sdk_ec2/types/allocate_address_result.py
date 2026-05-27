"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateAddressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.domain_type
    import aws_sdk_ec2.types.string


class AllocateAddressResult(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID that represents the allocation of the Elastic IP address.</p>"""
    public_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an address pool that you own.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.</p>"""
    domain: NotRequired["aws_sdk_ec2.types.domain_type.DomainType"]
    """<p>The network (<code>vpc</code>).</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address.</p>"""
    customer_owned_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer-owned address pool.</p>"""
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address. Available only for network interfaces that reside in a subnet in a Wavelength Zone.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon-owned IP address. Not available when using an address pool that you own.</p>"""

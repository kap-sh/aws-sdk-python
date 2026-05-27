"""Generated from Smithy shape ``com.amazonaws.ec2#Address``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.domain_type
    import aws_sdk_ec2.types.service_managed
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class Address(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID representing the allocation of the address.</p>"""
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID representing the association of the address with an instance.</p>"""
    domain: NotRequired["aws_sdk_ec2.types.domain_type.DomainType"]
    """<p>The network (<code>vpc</code>).</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    network_interface_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IP address associated with the Elastic IP address.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Elastic IP address.</p>"""
    public_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an address pool.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address.</p>"""
    customer_owned_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer-owned address pool.</p>"""
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address associated. This option is only available for network interfaces which reside in a subnet in a Wavelength Zone (for example an EC2 instance). </p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet where the IP address is allocated.</p>"""
    service_managed: NotRequired["aws_sdk_ec2.types.service_managed.ServiceManaged"]
    """<p>The service that manages the elastic IP address.</p> <note> <p>The only option supported today is <code>alb</code>.</p> </note>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance that the address is associated with (if any).</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""

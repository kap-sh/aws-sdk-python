"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredResourceCidr``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_double
    import aws_sdk_ec2.types.ipam_network_interface_attachment_status
    import aws_sdk_ec2.types.ipam_resource_cidr_ip_source
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.ipam_resource_tag_list
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class IpamDiscoveredResourceCidr(TypedDict):
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource Region.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource ID.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource owner ID.</p>"""
    resource_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource CIDR.</p>"""
    ip_source: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_cidr_ip_source.IpamResourceCidrIpSource"
    ]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The resource type.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>The resource tags.</p>"""
    ip_usage: NotRequired["aws_sdk_ec2.types.boxed_double.BoxedDouble"]
    """<p>The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:</p> <ul> <li> <p>For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs. </p> </li> <li> <p>For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated. </p> </li> <li> <p>For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs). </p> </li> </ul>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The VPC ID.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The subnet ID.</p>"""
    network_interface_attachment_status: NotRequired[
        "aws_sdk_ec2.types.ipam_network_interface_attachment_status.IpamNetworkInterfaceAttachmentStatus"
    ]
    """<p>For elastic network interfaces, this is the status of whether or not the elastic network interface is attached.</p>"""
    sample_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last successful resource discovery time.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone ID.</p>"""

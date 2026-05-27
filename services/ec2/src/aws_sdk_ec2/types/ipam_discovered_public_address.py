"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredPublicAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_association_status
    import aws_sdk_ec2.types.ipam_public_address_aws_service
    import aws_sdk_ec2.types.ipam_public_address_security_group_list
    import aws_sdk_ec2.types.ipam_public_address_tags
    import aws_sdk_ec2.types.ipam_public_address_type
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class IpamDiscoveredPublicAddress(TypedDict):
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    address_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the resource the IP address is assigned to.</p>"""
    address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address.</p>"""
    address_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner of the resource the IP address is assigned to.</p>"""
    address_allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID of the resource the IP address is assigned to.</p>"""
    association_status: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_association_status.IpamPublicAddressAssociationStatus"
    ]
    """<p>The association status.</p>"""
    address_type: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_type.IpamPublicAddressType"
    ]
    """<p>The IP address type.</p>"""
    service: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_aws_service.IpamPublicAddressAwsService"
    ]
    """<p>The Amazon Web Services service associated with the IP address.</p>"""
    service_resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource ARN or ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC that the resource with the assigned IP address is in.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet that the resource with the assigned IP address is in.</p>"""
    public_ipv4_pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the public IPv4 pool that the resource with the assigned IP address is from.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network interface ID of the resource with the assigned IP address.</p>"""
    network_interface_description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the network interface that IP address is assigned to.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance ID of the instance the assigned IP address is assigned to.</p>"""
    tags: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_tags.IpamPublicAddressTags"
    ]
    """<p>Tags associated with the IP address.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail\">Local Zone availability</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_security_group_list.IpamPublicAddressSecurityGroupList"
    ]
    """<p>Security groups associated with the resource that the IP address is assigned to.</p>"""
    sample_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last successful resource discovery time.</p>"""

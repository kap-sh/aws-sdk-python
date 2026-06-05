"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredPublicAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredPublicAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "address_region" in value:
        pairs.append((f"{prefix}.AddressRegion", str(value["address_region"])))
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "address_owner_id" in value:
        pairs.append((f"{prefix}.AddressOwnerId", str(value["address_owner_id"])))
    if "address_allocation_id" in value:
        pairs.append(
            (f"{prefix}.AddressAllocationId", str(value["address_allocation_id"]))
        )
    if "association_status" in value:
        import aws_sdk_ec2.types.ipam_public_address_association_status

        aws_sdk_ec2.types.ipam_public_address_association_status.serialize_ec2_query(
            value["association_status"], pairs, f"{prefix}.AssociationStatus"
        )
    if "address_type" in value:
        import aws_sdk_ec2.types.ipam_public_address_type

        aws_sdk_ec2.types.ipam_public_address_type.serialize_ec2_query(
            value["address_type"], pairs, f"{prefix}.AddressType"
        )
    if "service" in value:
        import aws_sdk_ec2.types.ipam_public_address_aws_service

        aws_sdk_ec2.types.ipam_public_address_aws_service.serialize_ec2_query(
            value["service"], pairs, f"{prefix}.Service"
        )
    if "service_resource" in value:
        pairs.append((f"{prefix}.ServiceResource", str(value["service_resource"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "public_ipv4_pool_id" in value:
        pairs.append((f"{prefix}.PublicIpv4PoolId", str(value["public_ipv4_pool_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "network_interface_description" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInterfaceDescription",
                str(value["network_interface_description"]),
            )
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.ipam_public_address_tags

        aws_sdk_ec2.types.ipam_public_address_tags.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "security_groups" in value:
        import aws_sdk_ec2.types.ipam_public_address_security_group_list

        aws_sdk_ec2.types.ipam_public_address_security_group_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroupSet"
        )
    if "sample_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sample_time"], pairs, f"{prefix}.SampleTime"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredPublicAddress:
    out: IpamDiscoveredPublicAddress = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_address_region = el.find("AddressRegion")
    if child_address_region is not None:
        out["address_region"] = str(child_address_region.text or "")
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_address_owner_id = el.find("AddressOwnerId")
    if child_address_owner_id is not None:
        out["address_owner_id"] = str(child_address_owner_id.text or "")
    child_address_allocation_id = el.find("AddressAllocationId")
    if child_address_allocation_id is not None:
        out["address_allocation_id"] = str(child_address_allocation_id.text or "")
    child_association_status = el.find("AssociationStatus")
    if child_association_status is not None:
        import aws_sdk_ec2.types.ipam_public_address_association_status

        out["association_status"] = (
            aws_sdk_ec2.types.ipam_public_address_association_status.deserialize_ec2_query(
                child_association_status
            )
        )
    child_address_type = el.find("AddressType")
    if child_address_type is not None:
        import aws_sdk_ec2.types.ipam_public_address_type

        out["address_type"] = (
            aws_sdk_ec2.types.ipam_public_address_type.deserialize_ec2_query(
                child_address_type
            )
        )
    child_service = el.find("Service")
    if child_service is not None:
        import aws_sdk_ec2.types.ipam_public_address_aws_service

        out["service"] = (
            aws_sdk_ec2.types.ipam_public_address_aws_service.deserialize_ec2_query(
                child_service
            )
        )
    child_service_resource = el.find("ServiceResource")
    if child_service_resource is not None:
        out["service_resource"] = str(child_service_resource.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_public_ipv4_pool_id = el.find("PublicIpv4PoolId")
    if child_public_ipv4_pool_id is not None:
        out["public_ipv4_pool_id"] = str(child_public_ipv4_pool_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_network_interface_description = el.find("NetworkInterfaceDescription")
    if child_network_interface_description is not None:
        out["network_interface_description"] = str(
            child_network_interface_description.text or ""
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_ec2.types.ipam_public_address_tags

        out["tags"] = aws_sdk_ec2.types.ipam_public_address_tags.deserialize_ec2_query(
            child_tags
        )
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    if el.find("SecurityGroupSet") is not None:
        import aws_sdk_ec2.types.ipam_public_address_security_group_list

        out["security_groups"] = (
            aws_sdk_ec2.types.ipam_public_address_security_group_list.deserialize_ec2_query(
                el, "SecurityGroupSet"
            )
        )
    child_sample_time = el.find("SampleTime")
    if child_sample_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["sample_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_sample_time
            )
        )
    return out

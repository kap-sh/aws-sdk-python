"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredResourceCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boxed_double
    import capo_ec2.types.ipam_network_interface_attachment_status
    import capo_ec2.types.ipam_resource_cidr_ip_source
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.ipam_resource_tag_list
    import capo_ec2.types.ipam_resource_type
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamDiscoveredResourceCidr(TypedDict, closed=True):
    ipam_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource Region.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource ID.</p>"""
    resource_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource owner ID.</p>"""
    resource_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource CIDR.</p>"""
    ip_source: NotRequired[
        "capo_ec2.types.ipam_resource_cidr_ip_source.IpamResourceCidrIpSource"
    ]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""
    resource_type: NotRequired["capo_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The resource type.</p>"""
    resource_tags: NotRequired[
        "capo_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>The resource tags.</p>"""
    ip_usage: NotRequired["capo_ec2.types.boxed_double.BoxedDouble"]
    """<p>The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:</p> <ul> <li> <p>For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs. </p> </li> <li> <p>For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated. </p> </li> <li> <p>For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs). </p> </li> </ul>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The VPC ID.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The subnet ID.</p>"""
    network_interface_attachment_status: NotRequired[
        "capo_ec2.types.ipam_network_interface_attachment_status.IpamNetworkInterfaceAttachmentStatus"
    ]
    """<p>For elastic network interfaces, this is the status of whether or not the elastic network interface is attached.</p>"""
    sample_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The last successful resource discovery time.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredResourceCidr, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_owner_id" in value:
        pairs.append((f"{key_prefix}ResourceOwnerId", str(value["resource_owner_id"])))
    if "resource_cidr" in value:
        pairs.append((f"{key_prefix}ResourceCidr", str(value["resource_cidr"])))
    if "ip_source" in value:
        import capo_ec2.types.ipam_resource_cidr_ip_source

        capo_ec2.types.ipam_resource_cidr_ip_source.serialize_ec2_query(
            value["ip_source"], pairs, f"{key_prefix}IpSource"
        )
    if "resource_type" in value:
        import capo_ec2.types.ipam_resource_type

        capo_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_tags" in value:
        import capo_ec2.types.ipam_resource_tag_list

        capo_ec2.types.ipam_resource_tag_list.serialize_ec2_query(
            value["resource_tags"], pairs, f"{key_prefix}ResourceTagSet"
        )
    if "ip_usage" in value:
        pairs.append((f"{key_prefix}IpUsage", str(value["ip_usage"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "network_interface_attachment_status" in value:
        import capo_ec2.types.ipam_network_interface_attachment_status

        capo_ec2.types.ipam_network_interface_attachment_status.serialize_ec2_query(
            value["network_interface_attachment_status"],
            pairs,
            f"{key_prefix}NetworkInterfaceAttachmentStatus",
        )
    if "sample_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sample_time"], pairs, f"{key_prefix}SampleTime"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredResourceCidr:
    out: IpamDiscoveredResourceCidr = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_id = el.find("ipamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_resource_region = el.find("resourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_owner_id = el.find("resourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_resource_cidr = el.find("resourceCidr")
    if child_resource_cidr is not None:
        out["resource_cidr"] = str(child_resource_cidr.text or "")
    child_ip_source = el.find("ipSource")
    if child_ip_source is not None:
        import capo_ec2.types.ipam_resource_cidr_ip_source

        out["ip_source"] = (
            capo_ec2.types.ipam_resource_cidr_ip_source.deserialize_ec2_query(
                child_ip_source
            )
        )
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_resource_type

        out["resource_type"] = capo_ec2.types.ipam_resource_type.deserialize_ec2_query(
            child_resource_type
        )
    if el.find("resourceTagSet") is not None:
        import capo_ec2.types.ipam_resource_tag_list

        out["resource_tags"] = (
            capo_ec2.types.ipam_resource_tag_list.deserialize_ec2_query(
                el, "resourceTagSet"
            )
        )
    child_ip_usage = el.find("ipUsage")
    if child_ip_usage is not None:
        out["ip_usage"] = float(child_ip_usage.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_network_interface_attachment_status = el.find(
        "networkInterfaceAttachmentStatus"
    )
    if child_network_interface_attachment_status is not None:
        import capo_ec2.types.ipam_network_interface_attachment_status

        out["network_interface_attachment_status"] = (
            capo_ec2.types.ipam_network_interface_attachment_status.deserialize_ec2_query(
                child_network_interface_attachment_status
            )
        )
    child_sample_time = el.find("sampleTime")
    if child_sample_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["sample_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_sample_time
        )
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out

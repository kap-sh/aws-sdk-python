"""Generated from Smithy shape ``com.amazonaws.ec2#Address``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Address, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "domain" in value:
        import aws_sdk_ec2.types.domain_type

        aws_sdk_ec2.types.domain_type.serialize_ec2_query(
            value["domain"], pairs, f"{prefix}.Domain"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "network_interface_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInterfaceOwnerId",
                str(value["network_interface_owner_id"]),
            )
        )
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "public_ipv4_pool" in value:
        pairs.append((f"{prefix}.PublicIpv4Pool", str(value["public_ipv4_pool"])))
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "customer_owned_ip" in value:
        pairs.append((f"{prefix}.CustomerOwnedIp", str(value["customer_owned_ip"])))
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (f"{prefix}.CustomerOwnedIpv4Pool", str(value["customer_owned_ipv4_pool"]))
        )
    if "carrier_ip" in value:
        pairs.append((f"{prefix}.CarrierIp", str(value["carrier_ip"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "service_managed" in value:
        import aws_sdk_ec2.types.service_managed

        aws_sdk_ec2.types.service_managed.serialize_ec2_query(
            value["service_managed"], pairs, f"{prefix}.ServiceManaged"
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))


def deserialize_ec2_query(el: Element) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_domain = el.find("Domain")
    if child_domain is not None:
        import aws_sdk_ec2.types.domain_type

        out["domain"] = aws_sdk_ec2.types.domain_type.deserialize_ec2_query(
            child_domain
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_network_interface_owner_id = el.find("NetworkInterfaceOwnerId")
    if child_network_interface_owner_id is not None:
        out["network_interface_owner_id"] = str(
            child_network_interface_owner_id.text or ""
        )
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_public_ipv4_pool = el.find("PublicIpv4Pool")
    if child_public_ipv4_pool is not None:
        out["public_ipv4_pool"] = str(child_public_ipv4_pool.text or "")
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_customer_owned_ip = el.find("CustomerOwnedIp")
    if child_customer_owned_ip is not None:
        out["customer_owned_ip"] = str(child_customer_owned_ip.text or "")
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_carrier_ip = el.find("CarrierIp")
    if child_carrier_ip is not None:
        out["carrier_ip"] = str(child_carrier_ip.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_service_managed = el.find("ServiceManaged")
    if child_service_managed is not None:
        import aws_sdk_ec2.types.service_managed

        out["service_managed"] = (
            aws_sdk_ec2.types.service_managed.deserialize_ec2_query(
                child_service_managed
            )
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    return out

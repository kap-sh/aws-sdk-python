"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesNetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_config_set
    import aws_sdk_ec2.types.scheduled_instances_ipv6_address_list
    import aws_sdk_ec2.types.scheduled_instances_security_group_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class ScheduledInstancesNetworkInterface(TypedDict):
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is <code>true</code>.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to delete the interface when the instance is terminated.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the device for the network interface attachment.</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_security_group_id_set.ScheduledInstancesSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_ipv6_address_list.ScheduledInstancesIpv6AddressList"
    ]
    """<p>The specific IPv6 addresses from the subnet range.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_address_configs: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_config_set.PrivateIpAddressConfigSet"
    ]
    """<p>The private IPv4 addresses.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesNetworkInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "associate_public_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.AssociatePublicIpAddress",
                "true" if value["associate_public_ip_address"] else "false",
            )
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "device_index" in value:
        pairs.append((f"{prefix}.DeviceIndex", str(value["device_index"])))
    if "groups" in value:
        import aws_sdk_ec2.types.scheduled_instances_security_group_id_set

        aws_sdk_ec2.types.scheduled_instances_security_group_id_set.serialize_ec2_query(
            value["groups"], pairs, f"{prefix}.Groups"
        )
    if "ipv6_address_count" in value:
        pairs.append((f"{prefix}.Ipv6AddressCount", str(value["ipv6_address_count"])))
    if "ipv6_addresses" in value:
        import aws_sdk_ec2.types.scheduled_instances_ipv6_address_list

        aws_sdk_ec2.types.scheduled_instances_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{prefix}.Ipv6Addresses"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))
    if "private_ip_address_configs" in value:
        import aws_sdk_ec2.types.private_ip_address_config_set

        aws_sdk_ec2.types.private_ip_address_config_set.serialize_ec2_query(
            value["private_ip_address_configs"],
            pairs,
            f"{prefix}.PrivateIpAddressConfigs",
        )
    if "secondary_private_ip_address_count" in value:
        pairs.append(
            (
                f"{prefix}.SecondaryPrivateIpAddressCount",
                str(value["secondary_private_ip_address_count"]),
            )
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesNetworkInterface:
    out: ScheduledInstancesNetworkInterface = {}  # type: ignore[typeddict-item]
    child_associate_public_ip_address = el.find("AssociatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    if el.find("Groups") is not None:
        import aws_sdk_ec2.types.scheduled_instances_security_group_id_set

        out["groups"] = (
            aws_sdk_ec2.types.scheduled_instances_security_group_id_set.deserialize_ec2_query(
                el, "Groups"
            )
        )
    child_ipv6_address_count = el.find("Ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    if el.find("Ipv6Addresses") is not None:
        import aws_sdk_ec2.types.scheduled_instances_ipv6_address_list

        out["ipv6_addresses"] = (
            aws_sdk_ec2.types.scheduled_instances_ipv6_address_list.deserialize_ec2_query(
                el, "Ipv6Addresses"
            )
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    if el.find("PrivateIpAddressConfigs") is not None:
        import aws_sdk_ec2.types.private_ip_address_config_set

        out["private_ip_address_configs"] = (
            aws_sdk_ec2.types.private_ip_address_config_set.deserialize_ec2_query(
                el, "PrivateIpAddressConfigs"
            )
        )
    child_secondary_private_ip_address_count = el.find("SecondaryPrivateIpAddressCount")
    if child_secondary_private_ip_address_count is not None:
        out["secondary_private_ip_address_count"] = int(
            child_secondary_private_ip_address_count.text or ""
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    return out

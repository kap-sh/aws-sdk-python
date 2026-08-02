"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_specification_response
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.instance_ipv4_prefix_list
    import capo_ec2.types.instance_ipv6_address_list
    import capo_ec2.types.instance_ipv6_prefix_list
    import capo_ec2.types.instance_network_interface_association
    import capo_ec2.types.instance_network_interface_attachment
    import capo_ec2.types.instance_private_ip_address_list
    import capo_ec2.types.network_interface_status
    import capo_ec2.types.operator_response
    import capo_ec2.types.string


class InstanceNetworkInterface(TypedDict, closed=True):
    association: NotRequired[
        "capo_ec2.types.instance_network_interface_association.InstanceNetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IPv4 associated with the network interface.</p>"""
    attachment: NotRequired[
        "capo_ec2.types.instance_network_interface_attachment.InstanceNetworkInterfaceAttachment"
    ]
    """<p>The network interface attachment.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description.</p>"""
    groups: NotRequired["capo_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses associated with the network interface.</p>"""
    mac_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The MAC address.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that created the network interface.</p>"""
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The private DNS name.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.instance_private_ip_address_list.InstancePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the network interface.</p>"""
    source_dest_check: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "capo_ec2.types.network_interface_status.NetworkInterfaceStatus"
    ]
    """<p>The status of the network interface.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    interface_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of network interface.</p> <p>Valid values: <code>interface</code> | <code>efa</code> | <code>efa-only</code> | <code>evs</code> | <code>trunk</code> </p>"""
    ipv4_prefixes: NotRequired[
        "capo_ec2.types.instance_ipv4_prefix_list.InstanceIpv4PrefixList"
    ]
    """<p>The IPv4 delegated prefixes that are assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired[
        "capo_ec2.types.instance_ipv6_prefix_list.InstanceIpv6PrefixList"
    ]
    """<p>The IPv6 delegated prefixes that are assigned to the network interface.</p>"""
    connection_tracking_configuration: NotRequired[
        "capo_ec2.types.connection_tracking_specification_response.ConnectionTrackingSpecificationResponse"
    ]
    r"""<p>A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association" in value:
        import capo_ec2.types.instance_network_interface_association

        capo_ec2.types.instance_network_interface_association.serialize_ec2_query(
            value["association"], pairs, f"{key_prefix}Association"
        )
    if "attachment" in value:
        import capo_ec2.types.instance_network_interface_attachment

        capo_ec2.types.instance_network_interface_attachment.serialize_ec2_query(
            value["attachment"], pairs, f"{key_prefix}Attachment"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.instance_ipv6_address_list

        capo_ec2.types.instance_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6AddressesSet"
        )
    if "mac_address" in value:
        pairs.append((f"{key_prefix}MacAddress", str(value["mac_address"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "private_dns_name" in value:
        pairs.append((f"{key_prefix}PrivateDnsName", str(value["private_dns_name"])))
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "private_ip_addresses" in value:
        import capo_ec2.types.instance_private_ip_address_list

        capo_ec2.types.instance_private_ip_address_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddressesSet"
        )
    if "source_dest_check" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDestCheck",
                "true" if value["source_dest_check"] else "false",
            )
        )
    if "status" in value:
        import capo_ec2.types.network_interface_status

        capo_ec2.types.network_interface_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "interface_type" in value:
        pairs.append((f"{key_prefix}InterfaceType", str(value["interface_type"])))
    if "ipv4_prefixes" in value:
        import capo_ec2.types.instance_ipv4_prefix_list

        capo_ec2.types.instance_ipv4_prefix_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4PrefixSet"
        )
    if "ipv6_prefixes" in value:
        import capo_ec2.types.instance_ipv6_prefix_list

        capo_ec2.types.instance_ipv6_prefix_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6PrefixSet"
        )
    if "connection_tracking_configuration" in value:
        import capo_ec2.types.connection_tracking_specification_response

        capo_ec2.types.connection_tracking_specification_response.serialize_ec2_query(
            value["connection_tracking_configuration"],
            pairs,
            f"{key_prefix}ConnectionTrackingConfiguration",
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> InstanceNetworkInterface:
    out: InstanceNetworkInterface = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import capo_ec2.types.instance_network_interface_association

        out["association"] = (
            capo_ec2.types.instance_network_interface_association.deserialize_ec2_query(
                child_association
            )
        )
    child_attachment = el.find("Attachment")
    if child_attachment is not None:
        import capo_ec2.types.instance_network_interface_attachment

        out["attachment"] = (
            capo_ec2.types.instance_network_interface_attachment.deserialize_ec2_query(
                child_attachment
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("GroupSet") is not None:
        import capo_ec2.types.group_identifier_list

        out["groups"] = capo_ec2.types.group_identifier_list.deserialize_ec2_query(
            el, "GroupSet"
        )
    if el.find("Ipv6AddressesSet") is not None:
        import capo_ec2.types.instance_ipv6_address_list

        out["ipv6_addresses"] = (
            capo_ec2.types.instance_ipv6_address_list.deserialize_ec2_query(
                el, "Ipv6AddressesSet"
            )
        )
    child_mac_address = el.find("MacAddress")
    if child_mac_address is not None:
        out["mac_address"] = str(child_mac_address.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    if el.find("PrivateIpAddressesSet") is not None:
        import capo_ec2.types.instance_private_ip_address_list

        out["private_ip_addresses"] = (
            capo_ec2.types.instance_private_ip_address_list.deserialize_ec2_query(
                el, "PrivateIpAddressesSet"
            )
        )
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        out["source_dest_check"] = (
            child_source_dest_check.text or ""
        ).lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.network_interface_status

        out["status"] = capo_ec2.types.network_interface_status.deserialize_ec2_query(
            child_status
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_interface_type = el.find("InterfaceType")
    if child_interface_type is not None:
        out["interface_type"] = str(child_interface_type.text or "")
    if el.find("Ipv4PrefixSet") is not None:
        import capo_ec2.types.instance_ipv4_prefix_list

        out["ipv4_prefixes"] = (
            capo_ec2.types.instance_ipv4_prefix_list.deserialize_ec2_query(
                el, "Ipv4PrefixSet"
            )
        )
    if el.find("Ipv6PrefixSet") is not None:
        import capo_ec2.types.instance_ipv6_prefix_list

        out["ipv6_prefixes"] = (
            capo_ec2.types.instance_ipv6_prefix_list.deserialize_ec2_query(
                el, "Ipv6PrefixSet"
            )
        )
    child_connection_tracking_configuration = el.find("ConnectionTrackingConfiguration")
    if child_connection_tracking_configuration is not None:
        import capo_ec2.types.connection_tracking_specification_response

        out["connection_tracking_configuration"] = (
            capo_ec2.types.connection_tracking_specification_response.deserialize_ec2_query(
                child_connection_tracking_configuration
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out

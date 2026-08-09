"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyNetworkInterfaceAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.attribute_value
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_specification_request
    import capo_ec2.types.ena_srd_specification
    import capo_ec2.types.network_interface_attachment_changes
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.subnet_id_list


class ModifyNetworkInterfaceAttributeRequest(TypedDict, closed=True):
    ena_srd_specification: NotRequired[
        "capo_ec2.types.ena_srd_specification.EnaSrdSpecification"
    ]
    """<p>Updates the ENA Express configuration for the network interface that’s attached to the instance.</p>"""
    enable_primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If you’re modifying a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    connection_tracking_specification: NotRequired[
        "capo_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A connection tracking specification.</p>"""
    associate_public_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).</p>"""
    associated_subnet_ids: NotRequired["capo_ec2.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to associate with the network interface.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    description: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>A description for the network interface.</p>"""
    source_dest_check: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is <code>true</code>, source/destination checks are enabled; otherwise, they are disabled. The default value is <code>true</code>. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.</p>"""
    groups: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.</p>"""
    attachment: NotRequired[
        "capo_ec2.types.network_interface_attachment_changes.NetworkInterfaceAttachmentChanges"
    ]
    """<p>Information about the interface attachment. If modifying the <code>delete on termination</code> attribute, you must specify the ID of the interface attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyNetworkInterfaceAttributeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ena_srd_specification" in value:
        import capo_ec2.types.ena_srd_specification

        capo_ec2.types.ena_srd_specification.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{key_prefix}EnaSrdSpecification"
        )
    if "enable_primary_ipv6" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePrimaryIpv6",
                "true" if value["enable_primary_ipv6"] else "false",
            )
        )
    if "connection_tracking_specification" in value:
        import capo_ec2.types.connection_tracking_specification_request

        capo_ec2.types.connection_tracking_specification_request.serialize_ec2_query(
            value["connection_tracking_specification"],
            pairs,
            f"{key_prefix}ConnectionTrackingSpecification",
        )
    if "associate_public_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}AssociatePublicIpAddress",
                "true" if value["associate_public_ip_address"] else "false",
            )
        )
    if "associated_subnet_ids" in value:
        import capo_ec2.types.subnet_id_list

        capo_ec2.types.subnet_id_list.serialize_ec2_query(
            value["associated_subnet_ids"], pairs, f"{key_prefix}AssociatedSubnetId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "description" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["description"], pairs, f"{key_prefix}Description"
        )
    if "source_dest_check" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["source_dest_check"], pairs, f"{key_prefix}SourceDestCheck"
        )
    if "groups" in value:
        import capo_ec2.types.security_group_id_string_list

        capo_ec2.types.security_group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "attachment" in value:
        import capo_ec2.types.network_interface_attachment_changes

        capo_ec2.types.network_interface_attachment_changes.serialize_ec2_query(
            value["attachment"], pairs, f"{key_prefix}Attachment"
        )


def deserialize_ec2_query(el: Element) -> ModifyNetworkInterfaceAttributeRequest:
    out: ModifyNetworkInterfaceAttributeRequest = {}  # type: ignore[typeddict-item]
    child_ena_srd_specification = el.find("EnaSrdSpecification")
    if child_ena_srd_specification is not None:
        import capo_ec2.types.ena_srd_specification

        out["ena_srd_specification"] = (
            capo_ec2.types.ena_srd_specification.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_enable_primary_ipv6 = el.find("EnablePrimaryIpv6")
    if child_enable_primary_ipv6 is not None:
        out["enable_primary_ipv6"] = (
            child_enable_primary_ipv6.text or ""
        ).lower() == "true"
    child_connection_tracking_specification = el.find("ConnectionTrackingSpecification")
    if child_connection_tracking_specification is not None:
        import capo_ec2.types.connection_tracking_specification_request

        out["connection_tracking_specification"] = (
            capo_ec2.types.connection_tracking_specification_request.deserialize_ec2_query(
                child_connection_tracking_specification
            )
        )
    child_associate_public_ip_address = el.find("AssociatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    child_associated_subnet_ids = el.find("AssociatedSubnetId")
    if child_associated_subnet_ids is not None:
        import capo_ec2.types.subnet_id_list

        out["associated_subnet_ids"] = (
            capo_ec2.types.subnet_id_list.deserialize_ec2_query(
                child_associated_subnet_ids
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        import capo_ec2.types.attribute_value

        out["description"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_description
        )
    child_source_dest_check = el.find("sourceDestCheck")
    if child_source_dest_check is not None:
        import capo_ec2.types.attribute_boolean_value

        out["source_dest_check"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_source_dest_check
            )
        )
    child_groups = el.find("SecurityGroupId")
    if child_groups is not None:
        import capo_ec2.types.security_group_id_string_list

        out["groups"] = (
            capo_ec2.types.security_group_id_string_list.deserialize_ec2_query(
                child_groups
            )
        )
    child_attachment = el.find("attachment")
    if child_attachment is not None:
        import capo_ec2.types.network_interface_attachment_changes

        out["attachment"] = (
            capo_ec2.types.network_interface_attachment_changes.deserialize_ec2_query(
                child_attachment
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceSecondaryInterfaceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.secondary_interface_private_ip_address_specification_list
    import capo_ec2.types.secondary_interface_type
    import capo_ec2.types.secondary_subnet_id


class LaunchTemplateInstanceSecondaryInterfaceSpecification(TypedDict, closed=True):
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the secondary interface is deleted when the instance is terminated.</p> <p>The only supported value for this field is <code>true</code>.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The device index for the secondary interface attachment.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.secondary_interface_private_ip_address_specification_list.SecondaryInterfacePrivateIpAddressSpecificationList"
    ]
    """<p>The private IPv4 addresses to assign to the secondary interface.</p> <p>If you specify <code>privateIpAddresses</code> you cannot specify <code>privateIpAddressCount</code> </p>"""
    private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of private IPv4 addresses to assign to the secondary interface.</p> <p>If you specify <code>privateIpAddressCount</code> you cannot specify <code>privateIpAddresses</code> </p>"""
    secondary_subnet_id: NotRequired[
        "capo_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    interface_type: NotRequired[
        "capo_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceSecondaryInterfaceSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))
    if "private_ip_addresses" in value:
        import capo_ec2.types.secondary_interface_private_ip_address_specification_list

        capo_ec2.types.secondary_interface_private_ip_address_specification_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddressesSet"
        )
    if "private_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}PrivateIpAddressCount",
                str(value["private_ip_address_count"]),
            )
        )
    if "secondary_subnet_id" in value:
        pairs.append(
            (f"{key_prefix}SecondarySubnetId", str(value["secondary_subnet_id"]))
        )
    if "interface_type" in value:
        import capo_ec2.types.secondary_interface_type

        capo_ec2.types.secondary_interface_type.serialize_ec2_query(
            value["interface_type"], pairs, f"{key_prefix}InterfaceType"
        )
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )


def deserialize_ec2_query(
    el: Element,
) -> LaunchTemplateInstanceSecondaryInterfaceSpecification:
    out: LaunchTemplateInstanceSecondaryInterfaceSpecification = {}  # type: ignore[typeddict-item]
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    if el.find("PrivateIpAddressesSet") is not None:
        import capo_ec2.types.secondary_interface_private_ip_address_specification_list

        out["private_ip_addresses"] = (
            capo_ec2.types.secondary_interface_private_ip_address_specification_list.deserialize_ec2_query(
                el, "PrivateIpAddressesSet"
            )
        )
    child_private_ip_address_count = el.find("PrivateIpAddressCount")
    if child_private_ip_address_count is not None:
        out["private_ip_address_count"] = int(child_private_ip_address_count.text or "")
    child_secondary_subnet_id = el.find("SecondarySubnetId")
    if child_secondary_subnet_id is not None:
        out["secondary_subnet_id"] = str(child_secondary_subnet_id.text or "")
    child_interface_type = el.find("InterfaceType")
    if child_interface_type is not None:
        import capo_ec2.types.secondary_interface_type

        out["interface_type"] = (
            capo_ec2.types.secondary_interface_type.deserialize_ec2_query(
                child_interface_type
            )
        )
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    return out

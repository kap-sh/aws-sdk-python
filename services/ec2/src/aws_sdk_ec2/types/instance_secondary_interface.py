"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_secondary_interface_attachment
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list
    import aws_sdk_ec2.types.secondary_interface_id
    import aws_sdk_ec2.types.secondary_interface_status
    import aws_sdk_ec2.types.secondary_interface_type
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.string


class InstanceSecondaryInterface(TypedDict, closed=True):
    attachment: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_attachment.InstanceSecondaryInterfaceAttachment"
    ]
    """<p>The attachment information for the secondary interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address of the secondary interface.</p>"""
    secondary_interface_id: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_id.SecondaryInterfaceId"
    ]
    """<p>The ID of the secondary interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the secondary interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list.InstanceSecondaryInterfacePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the secondary interface.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_status.SecondaryInterfaceStatus"
    ]
    """<p>The status of the secondary interface.</p>"""
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    interface_type: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attachment" in value:
        import aws_sdk_ec2.types.instance_secondary_interface_attachment

        aws_sdk_ec2.types.instance_secondary_interface_attachment.serialize_ec2_query(
            value["attachment"], pairs, f"{prefix}.Attachment"
        )
    if "mac_address" in value:
        pairs.append((f"{prefix}.MacAddress", str(value["mac_address"])))
    if "secondary_interface_id" in value:
        pairs.append(
            (f"{prefix}.SecondaryInterfaceId", str(value["secondary_interface_id"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "private_ip_addresses" in value:
        import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list

        aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{prefix}.PrivateIpAddressSet"
        )
    if "source_dest_check" in value:
        pairs.append(
            (
                f"{prefix}.SourceDestCheck",
                "true" if value["source_dest_check"] else "false",
            )
        )
    if "status" in value:
        import aws_sdk_ec2.types.secondary_interface_status

        aws_sdk_ec2.types.secondary_interface_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "secondary_subnet_id" in value:
        pairs.append((f"{prefix}.SecondarySubnetId", str(value["secondary_subnet_id"])))
    if "secondary_network_id" in value:
        pairs.append(
            (f"{prefix}.SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "interface_type" in value:
        import aws_sdk_ec2.types.secondary_interface_type

        aws_sdk_ec2.types.secondary_interface_type.serialize_ec2_query(
            value["interface_type"], pairs, f"{prefix}.InterfaceType"
        )


def deserialize_ec2_query(el: Element) -> InstanceSecondaryInterface:
    out: InstanceSecondaryInterface = {}  # type: ignore[typeddict-item]
    child_attachment = el.find("Attachment")
    if child_attachment is not None:
        import aws_sdk_ec2.types.instance_secondary_interface_attachment

        out["attachment"] = (
            aws_sdk_ec2.types.instance_secondary_interface_attachment.deserialize_ec2_query(
                child_attachment
            )
        )
    child_mac_address = el.find("MacAddress")
    if child_mac_address is not None:
        out["mac_address"] = str(child_mac_address.text or "")
    child_secondary_interface_id = el.find("SecondaryInterfaceId")
    if child_secondary_interface_id is not None:
        out["secondary_interface_id"] = str(child_secondary_interface_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("PrivateIpAddressSet") is not None:
        import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list

        out["private_ip_addresses"] = (
            aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list.deserialize_ec2_query(
                el, "PrivateIpAddressSet"
            )
        )
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        out["source_dest_check"] = (
            child_source_dest_check.text or ""
        ).lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.secondary_interface_status

        out["status"] = (
            aws_sdk_ec2.types.secondary_interface_status.deserialize_ec2_query(
                child_status
            )
        )
    child_secondary_subnet_id = el.find("SecondarySubnetId")
    if child_secondary_subnet_id is not None:
        out["secondary_subnet_id"] = str(child_secondary_subnet_id.text or "")
    child_secondary_network_id = el.find("SecondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_interface_type = el.find("InterfaceType")
    if child_interface_type is not None:
        import aws_sdk_ec2.types.secondary_interface_type

        out["interface_type"] = (
            aws_sdk_ec2.types.secondary_interface_type.deserialize_ec2_query(
                child_interface_type
            )
        )
    return out

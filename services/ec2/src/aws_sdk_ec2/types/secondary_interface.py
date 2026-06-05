"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.secondary_interface_attachment
    import aws_sdk_ec2.types.secondary_interface_id
    import aws_sdk_ec2.types.secondary_interface_ipv4_address_list
    import aws_sdk_ec2.types.secondary_interface_status
    import aws_sdk_ec2.types.secondary_interface_type
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecondaryInterface(TypedDict):
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the secondary interface.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the secondary interface.</p>"""
    attachment: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_attachment.SecondaryInterfaceAttachment"
    ]
    """<p>The attachment information for the secondary interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address of the secondary interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary interface.</p>"""
    private_ipv4_addresses: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_ipv4_address_list.SecondaryInterfaceIpv4AddressList"
    ]
    """<p>The private IPv4 addresses associated with the secondary interface.</p>"""
    secondary_interface_id: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_id.SecondaryInterfaceId"
    ]
    """<p>The ID of the secondary interface.</p>"""
    secondary_interface_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary interface.</p>"""
    secondary_interface_type: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_type: NotRequired[
        "aws_sdk_ec2.types.secondary_network_type.SecondaryNetworkType"
    ]
    """<p>The type of the secondary network.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_status.SecondaryInterfaceStatus"
    ]
    """<p>The status of the secondary interface.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "attachment" in value:
        import aws_sdk_ec2.types.secondary_interface_attachment

        aws_sdk_ec2.types.secondary_interface_attachment.serialize_ec2_query(
            value["attachment"], pairs, f"{prefix}.Attachment"
        )
    if "mac_address" in value:
        pairs.append((f"{prefix}.MacAddress", str(value["mac_address"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "private_ipv4_addresses" in value:
        import aws_sdk_ec2.types.secondary_interface_ipv4_address_list

        aws_sdk_ec2.types.secondary_interface_ipv4_address_list.serialize_ec2_query(
            value["private_ipv4_addresses"], pairs, f"{prefix}.PrivateIpv4AddressSet"
        )
    if "secondary_interface_id" in value:
        pairs.append(
            (f"{prefix}.SecondaryInterfaceId", str(value["secondary_interface_id"]))
        )
    if "secondary_interface_arn" in value:
        pairs.append(
            (f"{prefix}.SecondaryInterfaceArn", str(value["secondary_interface_arn"]))
        )
    if "secondary_interface_type" in value:
        import aws_sdk_ec2.types.secondary_interface_type

        aws_sdk_ec2.types.secondary_interface_type.serialize_ec2_query(
            value["secondary_interface_type"], pairs, f"{prefix}.SecondaryInterfaceType"
        )
    if "secondary_subnet_id" in value:
        pairs.append((f"{prefix}.SecondarySubnetId", str(value["secondary_subnet_id"])))
    if "secondary_network_id" in value:
        pairs.append(
            (f"{prefix}.SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "secondary_network_type" in value:
        import aws_sdk_ec2.types.secondary_network_type

        aws_sdk_ec2.types.secondary_network_type.serialize_ec2_query(
            value["secondary_network_type"], pairs, f"{prefix}.SecondaryNetworkType"
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
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> SecondaryInterface:
    out: SecondaryInterface = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_attachment = el.find("Attachment")
    if child_attachment is not None:
        import aws_sdk_ec2.types.secondary_interface_attachment

        out["attachment"] = (
            aws_sdk_ec2.types.secondary_interface_attachment.deserialize_ec2_query(
                child_attachment
            )
        )
    child_mac_address = el.find("MacAddress")
    if child_mac_address is not None:
        out["mac_address"] = str(child_mac_address.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("PrivateIpv4AddressSet") is not None:
        import aws_sdk_ec2.types.secondary_interface_ipv4_address_list

        out["private_ipv4_addresses"] = (
            aws_sdk_ec2.types.secondary_interface_ipv4_address_list.deserialize_ec2_query(
                el, "PrivateIpv4AddressSet"
            )
        )
    child_secondary_interface_id = el.find("SecondaryInterfaceId")
    if child_secondary_interface_id is not None:
        out["secondary_interface_id"] = str(child_secondary_interface_id.text or "")
    child_secondary_interface_arn = el.find("SecondaryInterfaceArn")
    if child_secondary_interface_arn is not None:
        out["secondary_interface_arn"] = str(child_secondary_interface_arn.text or "")
    child_secondary_interface_type = el.find("SecondaryInterfaceType")
    if child_secondary_interface_type is not None:
        import aws_sdk_ec2.types.secondary_interface_type

        out["secondary_interface_type"] = (
            aws_sdk_ec2.types.secondary_interface_type.deserialize_ec2_query(
                child_secondary_interface_type
            )
        )
    child_secondary_subnet_id = el.find("SecondarySubnetId")
    if child_secondary_subnet_id is not None:
        out["secondary_subnet_id"] = str(child_secondary_subnet_id.text or "")
    child_secondary_network_id = el.find("SecondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_secondary_network_type = el.find("SecondaryNetworkType")
    if child_secondary_network_type is not None:
        import aws_sdk_ec2.types.secondary_network_type

        out["secondary_network_type"] = (
            aws_sdk_ec2.types.secondary_network_type.deserialize_ec2_query(
                child_secondary_network_type
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
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

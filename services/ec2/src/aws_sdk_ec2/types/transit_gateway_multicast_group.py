"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.membership_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastGroup(TypedDict):
    group_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain group resource.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    group_member: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the resource is a transit gateway multicast group member.</p>"""
    group_source: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the resource is a transit gateway multicast group member.</p>"""
    member_type: NotRequired["aws_sdk_ec2.types.membership_type.MembershipType"]
    """<p>The member type (for example, <code>static</code>).</p>"""
    source_type: NotRequired["aws_sdk_ec2.types.membership_type.MembershipType"]
    """<p>The source type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_ip_address" in value:
        pairs.append((f"{prefix}.GroupIpAddress", str(value["group_ip_address"])))
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_owner_id" in value:
        pairs.append((f"{prefix}.ResourceOwnerId", str(value["resource_owner_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "group_member" in value:
        pairs.append(
            (f"{prefix}.GroupMember", "true" if value["group_member"] else "false")
        )
    if "group_source" in value:
        pairs.append(
            (f"{prefix}.GroupSource", "true" if value["group_source"] else "false")
        )
    if "member_type" in value:
        import aws_sdk_ec2.types.membership_type

        aws_sdk_ec2.types.membership_type.serialize_ec2_query(
            value["member_type"], pairs, f"{prefix}.MemberType"
        )
    if "source_type" in value:
        import aws_sdk_ec2.types.membership_type

        aws_sdk_ec2.types.membership_type.serialize_ec2_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastGroup:
    out: TransitGatewayMulticastGroup = {}  # type: ignore[typeddict-item]
    child_group_ip_address = el.find("GroupIpAddress")
    if child_group_ip_address is not None:
        out["group_ip_address"] = str(child_group_ip_address.text or "")
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_owner_id = el.find("ResourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_group_member = el.find("GroupMember")
    if child_group_member is not None:
        out["group_member"] = (child_group_member.text or "").lower() == "true"
    child_group_source = el.find("GroupSource")
    if child_group_source is not None:
        out["group_source"] = (child_group_source.text or "").lower() == "true"
    child_member_type = el.find("MemberType")
    if child_member_type is not None:
        import aws_sdk_ec2.types.membership_type

        out["member_type"] = aws_sdk_ec2.types.membership_type.deserialize_ec2_query(
            child_member_type
        )
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import aws_sdk_ec2.types.membership_type

        out["source_type"] = aws_sdk_ec2.types.membership_type.deserialize_ec2_query(
            child_source_type
        )
    return out

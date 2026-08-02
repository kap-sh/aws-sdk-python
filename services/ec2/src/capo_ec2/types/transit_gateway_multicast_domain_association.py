"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.subnet_association
    import capo_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastDomainAssociation(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain association resource.</p>"""
    subnet: NotRequired["capo_ec2.types.subnet_association.SubnetAssociation"]
    """<p>The subnet associated with the transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        capo_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_owner_id" in value:
        pairs.append((f"{key_prefix}ResourceOwnerId", str(value["resource_owner_id"])))
    if "subnet" in value:
        import capo_ec2.types.subnet_association

        capo_ec2.types.subnet_association.serialize_ec2_query(
            value["subnet"], pairs, f"{key_prefix}Subnet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainAssociation:
    out: TransitGatewayMulticastDomainAssociation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            capo_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_owner_id = el.find("ResourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_subnet = el.find("Subnet")
    if child_subnet is not None:
        import capo_ec2.types.subnet_association

        out["subnet"] = capo_ec2.types.subnet_association.deserialize_ec2_query(
            child_subnet
        )
    return out

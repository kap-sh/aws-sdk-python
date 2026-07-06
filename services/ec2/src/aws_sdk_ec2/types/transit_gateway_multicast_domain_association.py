"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_association
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastDomainAssociation(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain association resource.</p>"""
    subnet: NotRequired["aws_sdk_ec2.types.subnet_association.SubnetAssociation"]
    """<p>The subnet associated with the transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_owner_id" in value:
        pairs.append((f"{prefix}.ResourceOwnerId", str(value["resource_owner_id"])))
    if "subnet" in value:
        import aws_sdk_ec2.types.subnet_association

        aws_sdk_ec2.types.subnet_association.serialize_ec2_query(
            value["subnet"], pairs, f"{prefix}.Subnet"
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
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_owner_id = el.find("ResourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_subnet = el.find("Subnet")
    if child_subnet is not None:
        import aws_sdk_ec2.types.subnet_association

        out["subnet"] = aws_sdk_ec2.types.subnet_association.deserialize_ec2_query(
            child_subnet
        )
    return out

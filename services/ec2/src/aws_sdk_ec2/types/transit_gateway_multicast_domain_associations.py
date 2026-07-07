"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_association_list
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastDomainAssociations(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the resource.</p>"""
    subnets: NotRequired[
        "aws_sdk_ec2.types.subnet_association_list.SubnetAssociationList"
    ]
    """<p>The subnets associated with the multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainAssociations,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
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
    if "subnets" in value:
        import aws_sdk_ec2.types.subnet_association_list

        aws_sdk_ec2.types.subnet_association_list.serialize_ec2_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainAssociations:
    out: TransitGatewayMulticastDomainAssociations = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
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
    if el.find("Subnets") is not None:
        import aws_sdk_ec2.types.subnet_association_list

        out["subnets"] = (
            aws_sdk_ec2.types.subnet_association_list.deserialize_ec2_query(
                el, "Subnets"
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_association
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type
    import aws_sdk_ec2.types.transit_gateway_attachment_state


class TransitGatewayAttachment(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The resource type. Note that the <code>tgw-peering</code> resource type has been deprecated.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The attachment state. Note that the <code>initiating</code> state has been deprecated.</p>"""
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_association.TransitGatewayAttachmentAssociation"
    ]
    """<p>The association.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "transit_gateway_owner_id" in value:
        pairs.append(
            (f"{prefix}.TransitGatewayOwnerId", str(value["transit_gateway_owner_id"]))
        )
    if "resource_owner_id" in value:
        pairs.append((f"{prefix}.ResourceOwnerId", str(value["resource_owner_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        aws_sdk_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "association" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_association

        aws_sdk_ec2.types.transit_gateway_attachment_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )
    if "creation_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachment:
    out: TransitGatewayAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_owner_id = el.find("TransitGatewayOwnerId")
    if child_transit_gateway_owner_id is not None:
        out["transit_gateway_owner_id"] = str(child_transit_gateway_owner_id.text or "")
    child_resource_owner_id = el.find("ResourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    child_association = el.find("Association")
    if child_association is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_association

        out["association"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_association.deserialize_ec2_query(
                child_association
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.date_time

        out["creation_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

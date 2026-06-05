"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayPrefixListAttachment(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The resource type. Note that the <code>tgw-peering</code> resource type has been deprecated.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPrefixListAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "resource_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayPrefixListAttachment:
    out: TransitGatewayPrefixListAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
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
    return out

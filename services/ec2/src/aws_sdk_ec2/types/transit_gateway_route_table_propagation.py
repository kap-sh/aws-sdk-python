"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTablePropagation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type
    import aws_sdk_ec2.types.transit_gateway_propagation_state
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id


class TransitGatewayRouteTablePropagation(TypedDict):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource. Note that the <code>tgw-peering</code> resource type has been deprecated.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_propagation_state.TransitGatewayPropagationState"
    ]
    """<p>The state of the resource.</p>"""
    transit_gateway_route_table_announcement_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTablePropagation,
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
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_propagation_state

        aws_sdk_ec2.types.transit_gateway_propagation_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "transit_gateway_route_table_announcement_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableAnnouncementId",
                str(value["transit_gateway_route_table_announcement_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTablePropagation:
    out: TransitGatewayRouteTablePropagation = {}  # type: ignore[typeddict-item]
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
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_propagation_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_propagation_state.deserialize_ec2_query(
                child_state
            )
        )
    child_transit_gateway_route_table_announcement_id = el.find(
        "TransitGatewayRouteTableAnnouncementId"
    )
    if child_transit_gateway_route_table_announcement_id is not None:
        out["transit_gateway_route_table_announcement_id"] = str(
            child_transit_gateway_route_table_announcement_id.text or ""
        )
    return out

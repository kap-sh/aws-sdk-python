"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_attachment_list
    import aws_sdk_ec2.types.transit_gateway_route_state
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id
    import aws_sdk_ec2.types.transit_gateway_route_type


class TransitGatewayRoute(TypedDict, closed=True):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list used for destination matches.</p>"""
    transit_gateway_route_table_announcement_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement. </p>"""
    transit_gateway_attachments: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_attachment_list.TransitGatewayRouteAttachmentList"
    ]
    """<p>The attachments.</p>"""
    type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_type.TransitGatewayRouteType"
    ]
    """<p>The route type.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_state.TransitGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "transit_gateway_route_table_announcement_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableAnnouncementId",
                str(value["transit_gateway_route_table_announcement_id"]),
            )
        )
    if "transit_gateway_attachments" in value:
        import aws_sdk_ec2.types.transit_gateway_route_attachment_list

        aws_sdk_ec2.types.transit_gateway_route_attachment_list.serialize_ec2_query(
            value["transit_gateway_attachments"],
            pairs,
            f"{prefix}.TransitGatewayAttachments",
        )
    if "type" in value:
        import aws_sdk_ec2.types.transit_gateway_route_type

        aws_sdk_ec2.types.transit_gateway_route_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_route_state

        aws_sdk_ec2.types.transit_gateway_route_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRoute:
    out: TransitGatewayRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_transit_gateway_route_table_announcement_id = el.find(
        "TransitGatewayRouteTableAnnouncementId"
    )
    if child_transit_gateway_route_table_announcement_id is not None:
        out["transit_gateway_route_table_announcement_id"] = str(
            child_transit_gateway_route_table_announcement_id.text or ""
        )
    if el.find("TransitGatewayAttachments") is not None:
        import aws_sdk_ec2.types.transit_gateway_route_attachment_list

        out["transit_gateway_attachments"] = (
            aws_sdk_ec2.types.transit_gateway_route_attachment_list.deserialize_ec2_query(
                el, "TransitGatewayAttachments"
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.transit_gateway_route_type

        out["type"] = (
            aws_sdk_ec2.types.transit_gateway_route_type.deserialize_ec2_query(
                child_type
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_route_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_route_state.deserialize_ec2_query(
                child_state
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceTransitGatewayRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_route_table_id


class ReplaceTransitGatewayRouteRequest(TypedDict, closed=True):
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR range used for the destination match. Routing decisions are based on the most specific match.</p>"""
    transit_gateway_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the route table.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    blackhole: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether traffic matching this route is to be dropped.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceTransitGatewayRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "blackhole" in value:
        pairs.append(
            (f"{key_prefix}Blackhole", "true" if value["blackhole"] else "false")
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ReplaceTransitGatewayRouteRequest:
    out: ReplaceTransitGatewayRouteRequest = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_blackhole = el.find("Blackhole")
    if child_blackhole is not None:
        out["blackhole"] = (child_blackhole.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

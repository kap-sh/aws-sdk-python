"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class TransitGatewayRouteTableRoute(TypedDict, closed=True):
    destination_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state of the route.</p>"""
    route_origin: NotRequired["capo_ec2.types.string.String"]
    """<p>The route origin. The following are the possible values:</p> <ul> <li> <p>static</p> </li> <li> <p>propagated</p> </li> </ul>"""
    prefix_list_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the prefix list.</p>"""
    attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the route attachment.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource for the route attachment.</p>"""
    resource_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource type for the route attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTableRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr" in value:
        pairs.append((f"{key_prefix}DestinationCidr", str(value["destination_cidr"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "route_origin" in value:
        pairs.append((f"{key_prefix}RouteOrigin", str(value["route_origin"])))
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "attachment_id" in value:
        pairs.append((f"{key_prefix}AttachmentId", str(value["attachment_id"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableRoute:
    out: TransitGatewayRouteTableRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr = el.find("destinationCidr")
    if child_destination_cidr is not None:
        out["destination_cidr"] = str(child_destination_cidr.text or "")
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_route_origin = el.find("routeOrigin")
    if child_route_origin is not None:
        out["route_origin"] = str(child_route_origin.text or "")
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_attachment_id = el.find("attachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    return out

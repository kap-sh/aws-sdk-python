"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.local_gateway_routetable_id
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.string


class DeleteLocalGatewayRouteRequest(TypedDict, closed=True):
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR range for the route. This must match the CIDR for the route exactly.</p>"""
    local_gateway_route_table_id: NotRequired[
        "capo_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    destination_prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p> Use a prefix list in place of <code>DestinationCidrBlock</code>. You cannot use <code>DestinationPrefixListId</code> and <code>DestinationCidrBlock</code> in the same request. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayRouteRequest:
    out: DeleteLocalGatewayRouteRequest = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_destination_prefix_list_id = el.find("DestinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    return out

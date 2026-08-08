"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.local_gateway_max_results
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set
    import capo_ec2.types.string


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest(
    TypedDict, closed=True
):
    local_gateway_route_table_virtual_interface_group_association_ids: NotRequired[
        "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set.LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet"
    ]
    """<p>The IDs of the associations.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>local-gateway-id</code> - The ID of a local gateway.</p> </li> <li> <p> <code>local-gateway-route-table-arn</code> - The Amazon Resource Name (ARN) of the local gateway route table for the virtual interface group.</p> </li> <li> <p> <code>local-gateway-route-table-id</code> - The ID of the local gateway route table.</p> </li> <li> <p> <code>local-gateway-route-table-virtual-interface-group-association-id</code> - The ID of the association.</p> </li> <li> <p> <code>local-gateway-route-table-virtual-interface-group-id</code> - The ID of the virtual interface group.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the local gateway virtual interface group association.</p> </li> <li> <p> <code>state</code> - The state of the association.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.local_gateway_max_results.LocalGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_virtual_interface_group_association_ids" in value:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set

        capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set.serialize_ec2_query(
            value["local_gateway_route_table_virtual_interface_group_association_ids"],
            pairs,
            f"{key_prefix}LocalGatewayRouteTableVirtualInterfaceGroupAssociationId",
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest:
    out: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayRouteTableVirtualInterfaceGroupAssociationId") is not None:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set

        out["local_gateway_route_table_virtual_interface_group_association_ids"] = (
            capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set.deserialize_ec2_query(
                el, "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
            )
        )
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

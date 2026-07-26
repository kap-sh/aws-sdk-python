"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkRoutesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_segment_edge_identifier
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.network_route_list
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.route_table_type


class GetNetworkRoutesResponse(TypedDict, closed=True):
    route_table_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the route table.</p>"""
    core_network_segment_edge: NotRequired[
        "capo_networkmanager.types.core_network_segment_edge_identifier.CoreNetworkSegmentEdgeIdentifier"
    ]
    """<p>Describes a core network segment edge.</p>"""
    route_table_type: NotRequired[
        "capo_networkmanager.types.route_table_type.RouteTableType"
    ]
    """<p>The route table type.</p>"""
    route_table_timestamp: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The route table creation time.</p>"""
    network_routes: NotRequired[
        "capo_networkmanager.types.network_route_list.NetworkRouteList"
    ]
    """<p>The network routes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkRoutesResponse) -> dict:
    out: dict = {}
    if "route_table_arn" in value:
        out["RouteTableArn"] = value["route_table_arn"]
    if "core_network_segment_edge" in value:
        import capo_networkmanager.types.core_network_segment_edge_identifier

        out["CoreNetworkSegmentEdge"] = (
            capo_networkmanager.types.core_network_segment_edge_identifier.serialize_json(
                value["core_network_segment_edge"]
            )
        )
    if "route_table_type" in value:
        import capo_networkmanager.types.route_table_type

        out["RouteTableType"] = (
            capo_networkmanager.types.route_table_type.serialize_json(
                value["route_table_type"]
            )
        )
    if "route_table_timestamp" in value:
        import capo_networkmanager.types.date_time

        out["RouteTableTimestamp"] = capo_networkmanager.types.date_time.serialize_json(
            value["route_table_timestamp"]
        )
    if "network_routes" in value:
        import capo_networkmanager.types.network_route_list

        out["NetworkRoutes"] = (
            capo_networkmanager.types.network_route_list.serialize_json(
                value["network_routes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetNetworkRoutesResponse:
    out: GetNetworkRoutesResponse = {}  # type: ignore[typeddict-item]
    if "RouteTableArn" in data:
        out["route_table_arn"] = data["RouteTableArn"]
    if "CoreNetworkSegmentEdge" in data:
        import capo_networkmanager.types.core_network_segment_edge_identifier

        out["core_network_segment_edge"] = (
            capo_networkmanager.types.core_network_segment_edge_identifier.deserialize_json(
                data["CoreNetworkSegmentEdge"]
            )
        )
    if "RouteTableType" in data:
        import capo_networkmanager.types.route_table_type

        out["route_table_type"] = (
            capo_networkmanager.types.route_table_type.deserialize_json(
                data["RouteTableType"]
            )
        )
    if "RouteTableTimestamp" in data:
        import capo_networkmanager.types.date_time

        out["route_table_timestamp"] = (
            capo_networkmanager.types.date_time.deserialize_json(
                data["RouteTableTimestamp"]
            )
        )
    if "NetworkRoutes" in data:
        import capo_networkmanager.types.network_route_list

        out["network_routes"] = (
            capo_networkmanager.types.network_route_list.deserialize_json(
                data["NetworkRoutes"]
            )
        )
    return out

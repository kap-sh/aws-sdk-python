"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkRoute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.network_route_destination_list
    import aws_sdk_networkmanager.types.route_state
    import aws_sdk_networkmanager.types.route_type


class NetworkRoute(TypedDict):
    destination_cidr_block: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A unique identifier for the route, such as a CIDR block.</p>"""
    destinations: NotRequired[
        "aws_sdk_networkmanager.types.network_route_destination_list.NetworkRouteDestinationList"
    ]
    """<p>The destinations.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the prefix list.</p>"""
    state: NotRequired["aws_sdk_networkmanager.types.route_state.RouteState"]
    """<p>The route state. The possible values are <code>active</code> and <code>blackhole</code>.</p>"""
    type: NotRequired["aws_sdk_networkmanager.types.route_type.RouteType"]
    """<p>The route type. The possible values are <code>propagated</code> and <code>static</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkRoute) -> dict:
    out: dict = {}
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destinations" in value:
        import aws_sdk_networkmanager.types.network_route_destination_list

        out["Destinations"] = (
            aws_sdk_networkmanager.types.network_route_destination_list.serialize_json(
                value["destinations"]
            )
        )
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "state" in value:
        import aws_sdk_networkmanager.types.route_state

        out["State"] = aws_sdk_networkmanager.types.route_state.serialize_json(
            value["state"]
        )
    if "type" in value:
        import aws_sdk_networkmanager.types.route_type

        out["Type"] = aws_sdk_networkmanager.types.route_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> NetworkRoute:
    out: NetworkRoute = {}  # type: ignore[typeddict-item]
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if "Destinations" in data:
        import aws_sdk_networkmanager.types.network_route_destination_list

        out["destinations"] = (
            aws_sdk_networkmanager.types.network_route_destination_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "PrefixListId" in data:
        out["prefix_list_id"] = data["PrefixListId"]
    if "State" in data:
        import aws_sdk_networkmanager.types.route_state

        out["state"] = aws_sdk_networkmanager.types.route_state.deserialize_json(
            data["State"]
        )
    if "Type" in data:
        import aws_sdk_networkmanager.types.route_type

        out["type"] = aws_sdk_networkmanager.types.route_type.deserialize_json(
            data["Type"]
        )
    return out

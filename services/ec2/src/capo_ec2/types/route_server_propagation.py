"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_id
    import capo_ec2.types.route_server_propagation_state
    import capo_ec2.types.route_table_id


class RouteServerPropagation(TypedDict, closed=True):
    route_server_id: NotRequired["capo_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server configured for route propagation.</p>"""
    route_table_id: NotRequired["capo_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table configured for route server propagation.</p>"""
    state: NotRequired[
        "capo_ec2.types.route_server_propagation_state.RouteServerPropagationState"
    ]
    """<p>The current state of route propagation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerPropagation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_id" in value:
        pairs.append((f"{key_prefix}RouteServerId", str(value["route_server_id"])))
    if "route_table_id" in value:
        pairs.append((f"{key_prefix}RouteTableId", str(value["route_table_id"])))
    if "state" in value:
        import capo_ec2.types.route_server_propagation_state

        capo_ec2.types.route_server_propagation_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> RouteServerPropagation:
    out: RouteServerPropagation = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("routeServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_route_table_id = el.find("routeTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.route_server_propagation_state

        out["state"] = (
            capo_ec2.types.route_server_propagation_state.deserialize_ec2_query(
                child_state
            )
        )
    return out

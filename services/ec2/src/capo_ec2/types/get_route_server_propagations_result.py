"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerPropagationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_propagations_list


class GetRouteServerPropagationsResult(TypedDict, closed=True):
    route_server_propagations: NotRequired[
        "capo_ec2.types.route_server_propagations_list.RouteServerPropagationsList"
    ]
    """<p>Information about the route propagations for the specified route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerPropagationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_propagations" in value:
        import capo_ec2.types.route_server_propagations_list

        capo_ec2.types.route_server_propagations_list.serialize_ec2_query(
            value["route_server_propagations"],
            pairs,
            f"{key_prefix}RouteServerPropagationSet",
        )


def deserialize_ec2_query(el: Element) -> GetRouteServerPropagationsResult:
    out: GetRouteServerPropagationsResult = {}  # type: ignore[typeddict-item]
    if el.find("routeServerPropagationSet") is not None:
        import capo_ec2.types.route_server_propagations_list

        out["route_server_propagations"] = (
            capo_ec2.types.route_server_propagations_list.deserialize_ec2_query(
                el, "routeServerPropagationSet"
            )
        )
    return out
